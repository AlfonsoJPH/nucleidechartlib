from enum import Enum

# Enum for the type of decay
class DecayMode(Enum):
    ALPHA = "Alpha" # a Alpha emission
    BETA_PLUS = "Beta+" # b+ Positron emission
    BETA_MINUS = "Beta-" # b- Negatron emission
    ELECTRON_CAPTURE = "Electron Capture" # ec Electron capture
    PROTON = "Proton" # p Proton emission
    NEUTRON = "Neutron" # n Neutron emission
    SF = "Spontaneous Fission" # sf Spontaenous fission
    STABLE = "Stable" # s Stable
    IT = "Isomeric Transition" # it Isomeric Transition
