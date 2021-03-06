import dataclasses
from typing import Generator, List, Tuple, Dict, Optional
import requests

from .mof import Mof


def unit_conversion_headers(pressure_unit: str = None, loading_unit: str = None) -> Optional[Dict[str, str]]:
    # Build unit conversion headers if pressure/loading units are supplied.
    if pressure_unit or loading_unit:
        headers = {}
        # Download valid units
        r = requests.get('https://mof.tech.northwestern.edu/classifications.json')
        classifications = r.json()
        # Sort into pressure/loading units
        pressure_units = [cls['name'] for cls in classifications if cls["type"] == "pressure"]
        loading_units = [cls['name'] for cls in classifications if cls["type"] == "loading"]
        # Raise errors if invalid
        if pressure_unit is not None and pressure_unit not in pressure_units:
            raise InvalidUnit(
                f"'{pressure_unit}' is not a valid unit for pressure. Valid pressure units are: {pressure_units}")
        if loading_unit is not None and loading_unit not in loading_units:
            raise InvalidUnit(
                f"'{loading_unit}' is not a valid unit for loading. Valid loading units are: {loading_units}")
        # Add to headers if unit was specified
        if loading_unit:
            headers["loading"] = loading_unit
        if pressure_unit:
            headers["pressure"] = pressure_unit
        return headers
    return None


def get_page(params, headers: Dict[str, str], page=1) -> Tuple[List[Mof], int]:
    """Download 1 page from the api returns List[Mof] + total # of pages"""
    if page and page != 1:
        params["page"] = page
    r = requests.get('https://mof.tech.northwestern.edu/mofs.json', headers=headers, params=params)
    json_response = r.json()
    return [Mof(x) for x in json_response['results']], json_response["pages"]


def get_all(params: Dict[str, str], pressure_unit: str = None, loading_unit: str = None) -> Generator[Mof, None, None]:
    page = 1
    pages = 2
    headers = unit_conversion_headers(pressure_unit, loading_unit)
    while page <= pages:
        mofs, pages = get_page(params, headers, page)
        yield from mofs
        page += 1


class InvalidUnit(Exception):
    pass


def fetch(mofid: str = None,
          mofkey: str = None,
          vf_min: float = None,
          vf_max: float = None,
          lcd_min: float = None,
          lcd_max: float = None,
          pld_min: float = None,
          pld_max: float = None,
          sa_m2g_min: float = None,
          sa_m2g_max: float = None,
          sa_m2cm3_min: float = None,
          sa_m2cm3_max: float = None,
          telemetry: bool = True,
          pressure_unit: str = None,
          loading_unit: str = None,
          limit: int = None) -> Generator[Mof, None, None]:
    """Return all mofs that match the args supplied by querying the mofdb API"""
    if telemetry:
        # Catch, log, and re-raise exceptions in telemetry mode
        try:
            yield from fetch_inner(mofid=mofid, mofkey=mofkey, vf_min=vf_min, vf_max=vf_max, lcd_min=lcd_min,
                                   lcd_max=lcd_max, pld_min=pld_min, pld_max=pld_max, sa_m2g_min=sa_m2g_min,
                                   sa_m2g_max=sa_m2g_max, sa_m2cm3_min=sa_m2cm3_min,
                                   sa_m2cm3_max=sa_m2cm3_max, pressure_unit=pressure_unit, loading_unit=loading_unit,
                                   limit=limit)
        except Exception as e:
            import sentry_sdk
            sentry_sdk.init("https://287d83a67df94a3288777a876182cfcc@o310079.ingest.sentry.io/6290292",
                            traces_sample_rate=0.0)
            sentry_sdk.capture_exception(e)
            raise e
    else:
        yield from fetch_inner(mofid=mofid, mofkey=mofkey, vf_min=vf_min, vf_max=vf_max, lcd_min=lcd_min,
                               lcd_max=lcd_max, pld_min=pld_min, pld_max=pld_max, sa_m2g_min=sa_m2g_min,
                               sa_m2g_max=sa_m2g_max, sa_m2cm3_min=sa_m2cm3_min,
                               sa_m2cm3_max=sa_m2cm3_max, pressure_unit=pressure_unit, loading_unit=loading_unit,
                               limit=limit)


def fetch_inner(
        mofid: str = None,
        mofkey: str = None,
        vf_min: float = None,
        vf_max: float = None,
        lcd_min: float = None,
        lcd_max: float = None,
        pld_min: float = None,
        pld_max: float = None,
        sa_m2g_min: float = None,
        sa_m2g_max: float = None,
        sa_m2cm3_min: float = None,
        sa_m2cm3_max: float = None,
        pressure_unit: str = None,
        loading_unit: str = None,
        limit: int = None) -> Generator[Mof, None, None]:
    """Telemetry blind fetch function. Handles building params and stopping when limit is reached"""
    params = {}
    if mofid:
        params["mofid"] = mofid
    if mofkey:
        params["mofkey"] = mofkey
    if limit:
        params["limit"] = limit
    if vf_min:
        params["vf_min"] = vf_min
    if vf_max:
        params["vf_max"] = vf_max
    if lcd_min:
        params["lcd_min"] = lcd_min
    if lcd_max:
        params["lcd_max"] = lcd_max
    if pld_min:
        params["pld_min"] = pld_min
    if pld_max:
        params["pld_max"] = pld_max
    if sa_m2g_min:
        params["sa_m2g_min"] = sa_m2g_min
    if sa_m2g_max:
        params["sa_m2g_max"] = sa_m2g_max
    if sa_m2cm3_min:
        params["sa_m2cm3_min"] = sa_m2cm3_min
    if sa_m2cm3_max:
        params["sa_m2cm3_max"] = sa_m2cm3_max

    if limit:
        yielded = 0
        mofs = get_all(params, pressure_unit=pressure_unit, loading_unit=loading_unit)
        while yielded < limit:
            yield mofs.__next__()
            yielded += 1

    else:
        yield from get_all(params, pressure_unit=pressure_unit, loading_unit=loading_unit)
