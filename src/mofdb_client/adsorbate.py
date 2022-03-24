import dataclasses


@dataclasses.dataclass
class Adsorbate:
    def __init__(self, json: dict):
        self.id = json["id"]
        self.InChIKey = json["InChIKey"]
        self.name = json["name"]
        self.InChICode = json["InChICode"]
        self.formula = json["formula"]
    id: int
    InChIKey: str
    name: str
    InChICode: str
    formula: str