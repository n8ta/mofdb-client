import dataclasses
from typing import Generator, List, Tuple, Dict, Optional
import requests

from .mof import Mof


def get_page(params, page=1) -> Tuple[List[Mof], int]:
    if page and page != 1:
        params["page"] = page
    r = requests.get('https://mofs.tech.northwestern.edu/mofs.json', params=params)
    json_response = r.json()
    return [Mof(x) for x in json_response['results']], json_response["pages"]


def get_all(params: Dict[str, str]) -> Generator[Mof, None, None]:
    page = 1
    pages = 2
    while page <= pages:
        mofs, pages = get_page(params, page)
        yield from mofs
        page += 1


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
          limit: int = None) -> Generator[Mof, None, None]:
    if telemetry:
        try:
            yield from fetch_inner(mofid=mofid, mofkey=mofkey, vf_min=vf_min, vf_max=vf_max, lcd_min=lcd_min,
                               lcd_max=lcd_max, pld_min=pld_min, pld_max=pld_max, sa_m2g_min=sa_m2g_min,
                               sa_m2g_max=sa_m2g_max, sa_m2cm3_min=sa_m2cm3_min,
                               sa_m2cm3_max=sa_m2cm3_max, limit=limit)
        except Exception as e:
            import sentry_sdk
            sentry_sdk.init("https://287d83a67df94a3288777a876182cfcc@o310079.ingest.sentry.io/6290292", traces_sample_rate=0.0)
            sentry_sdk.capture_exception(e)
            raise e
    else:
        yield from fetch_inner(mofid=mofid, mofkey=mofkey, vf_min=vf_min, vf_max=vf_max, lcd_min=lcd_min,
                               lcd_max=lcd_max, pld_min=pld_min, pld_max=pld_max, sa_m2g_min=sa_m2g_min,
                               sa_m2g_max=sa_m2g_max, sa_m2cm3_min=sa_m2cm3_min,
                               sa_m2cm3_max=sa_m2cm3_max, limit=limit)


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
        limit: int = None) -> Generator[Mof, None, None]:
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
        mofs = get_all(params)
        while yielded < limit:
            yield mofs.__next__()
            yielded += 1

    else:
        yield from get_all(params)
