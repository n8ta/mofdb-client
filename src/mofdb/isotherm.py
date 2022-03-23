import dataclasses
from typing import List, Optional

from .adsorbate import Adsorbate
from .adsorbent import Adsorbent
from .temperature_point import TemperaturePoint

@dataclasses.dataclass
class Isotherm:
    def __init__(self, json: dict):
        self.id = json["id"]
        self.isotherm_data = [TemperaturePoint(i) for i in json["isotherm_data"]]
        self.batch_number = json["batch_number"]
        self.adsorbates = [Adsorbate(a) for a in json["adsorbates"]]
        self.digitizer = json["digitizer"]
        self.simin = json["simin"]
        self.DOI = json["DOI"]
        self.date = json["date"]
        self.temperature = json["temperature"]
        self.adsorbent_forcefield = json["adsorbent_forcefield"]
        self.molecule_forcefield = json["molecule_forcefield"]
        self.adsorbent = Adsorbent(json["adsorbent"])
        self.category = json["category"]
        self.adsorptionUnits = json["adsorptionUnits"]
        self.pressureUnits = json["pressureUnits"]
        self.compositionType = json["compositionType"]
        self.isotherm_url = json["isotherm_url"]
    id: int
    isotherm_data: List[TemperaturePoint]
    batch_number: Optional[int]
    adsorbates: List[Adsorbate]
    digitizer: str
    simin: str
    DOI: str
    date: str
    temperature: float
    adsorbent_forcefield: str
    molecule_forcefield: str
    adsorbent: Adsorbent
    category: str
    adsorptionUnits: str
    pressureUnits: str
    compositionType: str
    isotherm_url: str

