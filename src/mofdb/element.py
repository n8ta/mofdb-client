import dataclasses
from typing import List


@dataclasses.dataclass
class Element:
    """Eg: Element(symbol: Zn, name: Zinc)"""
    def __init__(self, json: dict):
        self.symbol = json["symbol"]
        self.name = json["name"]
    symbol: str
    name: str
