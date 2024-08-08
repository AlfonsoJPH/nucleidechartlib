from dataclasses import dataclass
from typing import Dict
from nucleidechartlib.element.nucleide import Nucleide

# Definición de la clase Nucleide
@dataclass
class Element:
    id: int
    mass_number: int
    atomic_number: int
    symbol: str
    nucleides: Dict[int, Nucleide]




    def __repr__(self):
        return f"{self.symbol}{self.mass_number}"

    # def add
