from enum import Enum

# Enum for the type of decay
class DecayMode(Enum):
    ALPHA = "Alpha" # a Alpha emission
    BETA_PLUS = "Beta+" # b+ Positron emission
    BETA_MINUS = "Beta-" # b- Negatron emission
    ELECTRON_CAPTURE = "EC" # ec Electron capture
    GAMMA = "Gamma" # g Gamma emission
    ISOMER = "Isomer" # i Isomer emission
    PROTON = "Proton" # p Proton emission
    NEUTRON = "Neutron" # n Neutron emission
    SF = "SF" # sf Spontaenous fission
    STABLE = "Stable" # s Stable
    IT = "Isomeric Transition" # it Isomeric Transition
