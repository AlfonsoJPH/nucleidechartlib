from ..enums import DecayMode
from dataclasses import dataclass
from typing import Dict, Optional

# Definición de la clase Nucleide
@dataclass
class Nucleide:
    id: int
    mass_excess: float
    half_life: str
    decay_modes_intensities: Dict[DecayMode, float]
    energy_levels: Dict[str, float]
    spin_and_parity: str
    year_of_discovery: int


    def get_highest_priority_decay_mode(self) -> Optional[DecayMode]:
        if not self.decay_modes_intensities:
            return None

        return max(self.decay_modes_intensities, key=lambda mode: self.decay_modes_intensities[mode])

    def __repr__(self):
        highest_priority_mode = self.get_highest_priority_decay_mode()
        return f"{self.spin_and_parity} {self.year_of_discovery} {highest_priority_mode.name if highest_priority_mode else 'None'}"
