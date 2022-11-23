import dataclasses
from typing import Optional, List
from .adsorbate import Adsorbate
from .isotherm import Isotherm
from .element import Element

@dataclasses.dataclass
class Mof:
    def __init__(self, json: dict):
        self.name = json["name"]
        self.id = json["id"]
        self.cif = json["cif"]
        self.isotherms = [Isotherm(iso) for iso in json["isotherms"]]
        self.heats = [Isotherm(iso) for iso in json["heats"]]
        self.void_fraction = json["void_fraction"]
        self.surface_area_m2g = json["surface_area_m2g"]
        self.surface_area_m2cm3 = json["surface_area_m2cm3"]
        self.pld = json["pld"]
        self.lcd = json["lcd"]
        self.pxrd = json["pxrd"]
        self.pore_size_distribution = json["pore_size_distribution"]
        self.database = json["database"]
        self.cif = json["cif"]
        self.url = json["url"]
        self.adsorbates = [Adsorbate(ads) for ads in json["adsorbates"]]
        self.elements = [Element(el) for el in json["elements"]]
        self.mofid = json["mofid"]
        self.mofkey = json["mofkey"]
        self.batch_number = json["batch_number"]
        self.json_repr = json

    id: int
    name: str
    cif: str
    isotherms: List[Isotherm]
    heats: List[Isotherm]
    void_fraction: Optional[float]
    surface_area_m2g: Optional[float]
    surface_area_m2cm3: Optional[float]
    pld: Optional[float]
    lcd: Optional[float]
    pxrd: Optional[str]
    pore_size_distribution: Optional[str]
    database: str
    cif: str
    url: str
    adsorbates: List[Adsorbate]
    elements: List[Element]
    mofid: Optional[str]
    mofkey: Optional[str]
    batch_number: Optional[int]
    json_repr: dict