import dataclasses
from typing import Generator
import requests

from .mof import Mof


def fetch(
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
    r = requests.get('https://mof.tech.northwestern.edu/mofs.json', params=params)
    res = [Mof(x) for x in r.json()['results']]
    if limit:
        yield from res[0:limit]
    else:
        yield from res
