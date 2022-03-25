import dataclasses


@dataclasses.dataclass
class Adsorbent:
    def __init__(self, json: dict):
        self.id = json["id"]
        self.name = json["name"]
    id: int
    name: str
