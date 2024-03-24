from enum import Enum

# Enum for the type of decay
class DecayMode(Enum):
    ALPHA = 1 # a
    BETA_PLUS = 2 # b+
    BETA_MINUS = 3 # b-
    ELECTRON_CAPTURE = 4 # ec
    GAMMA = 5 # g
    ISOMER = 6 # i
    PROTON = 7 # p
    NEUTRON = 8 # n
    SF = 9 # sf

# Atributes of an element Mass Number,Atomic Number,A Element,Isomer,Mass Excess,Mass Excess uncertainty,Isomer Excitation Energy,Isomer Excitation Energy uncertainty,Origin of Excitation Energy,Isom.Unc,Isom.Inv,Half-life,Half-life unit,Half-life uncertainty,Spin and Parity,Ensdf year,Year of Discovery,Decay Modes and their Intensities
class Element:
    def __init__(self, symbol, atomic_number, atomic_weight):
        self._symbol = symbol
        self._atomic_number = atomic_number
        self.atomic_weight = atomic_weight
        self._ensdf_year = int()
        self._year_of_discovery = int()
        self.decay_modes_and_intensities = set()

    @property
    def symbol(self):
        return self._symbol

    @symbol.setter
    def symbol(self, value):
        if not isinstance(value, str):
            raise ValueError("Invalid symbol")
        self.symbol = value

    @property
    def atomic_number(self):
        return self._atomic_number

    @atomic_number.setter
    def atomic_number(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Invalid atomic number")
        self.atomic_number = value

    @property
    def isomer(self):
        return self.isomer

    @isomer.setter
    def isomer(self, value):
        if not isinstance(value, bool):
            raise ValueError("Invalid isomer")
        self.isomer = value

    @property
    def mass_excess(self):
        return self.mass_excess

    @mass_excess.setter
    def mass_excess(self, value):
        if not isinstance(value, float):
            raise ValueError("Invalid mass excess")
        self.mass_excess = value

    @property
    def mass_excess_uncertainty(self):
        return self.mass_excess_uncertainty

    @mass_excess_uncertainty.setter
    def mass_excess_uncertainty(self, value):
        if not isinstance(value, float):
            raise ValueError("Invalid mass excess uncertainty")
        self.mass_excess_uncertainty = value

    @property
    def isomer_excitation_energy(self):
        return self.isomer_excitation_energy

    @isomer_excitation_energy.setter
    def isomer_excitation_energy(self, value):
        if not isinstance(value, float):
            raise ValueError("Invalid isomer excitation energy")
        self.isomer_excitation_energy = value

    @property
    def isomer_excitation_energy_uncertainty(self):
        return self.isomer_excitation_energy_uncertainty

    @isomer_excitation_energy_uncertainty.setter
    def isomer_excitation_energy_uncertainty(self, value):
        if not isinstance(value, float):
            raise ValueError("Invalid isomer excitation energy uncertainty")
        self.isomer_excitation_energy_uncertainty = value

    @property
    def ensdf_year(self):
        return self.ensdf_year

    @ensdf_year.setter
    def ensdf_year(self, value):
        if not value is int or value < 0:
            raise ValueError("Invalid ensdf year")
        self.ensdf_year = value

    @property
    def year_of_discovery(self):
        return self.year_of_discovery

    @year_of_discovery.setter
    def year_of_discovery(self, value):
        if not value is int or value < 0:
            raise ValueError("Invalid year of discovery")
        self.year_of_discovery = value

    def add_decay_mode_and_intensity(self, decay_mode, intensity):
        if not isinstance(decay_mode, DecayMode):
            raise ValueError("Invalid decay mode")
        if decay_mode in self.decay_modes_and_intensities:
            raise ValueError("Decay mode already added")
        self.decay_modes_and_intensities.add({decay_mode, intensity})



    def set_origin_of_excitation_energy(self, origin_of_excitation_energy):
        self.origin_of_excitation_energy = origin_of_excitation_energy

    def set_isom_unc(self, isom_unc):
        self.isom_unc = isom_unc

    def set_isom_inv(self, isom_inv):
        self.isom_inv = isom_inv

    def set_half_life(self, half_life):
        self.half_life = half_life

    def set_half_life_unit(self, half_life_unit):
        self.half_life_unit = half_life_unit

    def set_half_life_uncertainty(self, half_life_uncertainty):
        self.half_life_uncertainty = half_life_uncertainty

    def set_spin_and_parity(self, spin_and_parity):
        self.spin_and_parity = spin_and_parity
