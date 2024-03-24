from enum import EnumMeta
import svgwrite
from .element import Element
from svgwrite.shapes import Rect

class ElementBox:
    def __init__(self, element:Element, width, height, stroke, stroke_width):
        self.element = element

        self.x = element.atomic_weight
        self.y = element.atomic_number
        self.width = width
        self.height = height
        self.stroke = stroke
        self.stroke_width = stroke_width


        self.symbol_size = 10
        self.atomic_number_size = 6
        self.atomic_weight_size = 6
        self.isomer_size = 6
        self.mass_excess_size = 6
        self.mass_excess_uncertainty_size = 6
        self.isomer_excitation_energy_size = 6
        self.isomer_excitation_energy_uncertainty_size = 6
        self.origin_of_excitation_energy_size = 6
        self.isom_unc_size = 6
        self.isom_inv_size = 6
        self.half_life_size = 6
        self.half_life_unit_size = 6
        self.half_life_uncertainty_size = 6
        self.spin_and_parity_size = 6
        self.ensdf_year_size = 6
        self.year_of_discovery_size = 6

        if len(element.decay_modes_and_intensities) > 0:
            fillBox = max(element.decay_modes_and_intensities, key=lambda k: element.decay_modes_and_intensities[k])
        else:
            fillBox = 'white'

        self.box = Rect((self.x, self.y), (self.width, self.height), id = (str(self.x) + element.symbol), fill=fillBox, stroke=self.stroke, stroke_width=self.stroke_width)

    def draw(self, dwg):
        dwg.add(self.box)
