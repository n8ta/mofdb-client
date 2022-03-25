import dataclasses
from typing import List


@dataclasses.dataclass
class GasAtTemp:
    """Adsorption is in the selected loading units and composition is based on the compositionType of the isotherm """
    def __init__(self, json: dict):
        self.InChIKey = json["InChIKey"]
        self.name = json["name"]
        self.composition = json["composition"]
        self.adsorption = json["adsorption"]
    InChIKey: str
    name: str
    composition: float
    adsorption: float

@dataclasses.dataclass
class TemperaturePoint:
    """A single temperature point on an isotherm. It may contain data for multiple different gases if this is a
    multicomponent isotherm. See the species_data field for adsorptions of each gas."""
    def __init__(self, json: dict):
        self.pressure = json["pressure"]
        self.total_adsorption = json["total_adsorption"]
        self.species_data = [GasAtTemp(x) for x in json["species_data"]]
    pressure: float
    species_data: List[GasAtTemp]
