from .element import DecayMode, Element

class ElementBox:
    def __init__(self, element:Element, width, height, stroke, stroke_width, total_width=3000, total_height=1250):
        self.element = element
        self.box = None

        self.x = int(element.atomic_weight)
        self.y = int(element.atomic_number)
        self.width = width
        self.height = height
        self.stroke = stroke
        self.stroke_width = stroke_width


        self.symbol_size = 0.8*width - len(element.symbol) * 0.1*width
        self.atomic_number_size = 0.2*width
        self.atomic_weight_size = 0.2*width
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

        self.total_width = total_width
        self.total_height = total_height

        if len(element.decay_modes_and_intensities) > 0:
            self.fillBox = self.get_decay_color()
        else:
            self.fillBox = 'white'


    def get_decay_color(self):
        switch_case = {
            DecayMode.ALPHA: 'red',
            DecayMode.BETA_PLUS: 'blue',
            DecayMode.BETA_MINUS: 'green',
            DecayMode.ELECTRON_CAPTURE: 'yellow',
            DecayMode.ISOMER: 'purple',
            DecayMode.PROTON: 'orange',
            DecayMode.NEUTRON: 'pink',
            DecayMode.SF: 'brown'
        }
        if self.element.decay_modes_and_intensities[0][0] in switch_case:
            return switch_case[self.element.decay_modes_and_intensities[0][0]]
        else:
            return 'white'


    def get_box_position(self):
        return self.x*self.width, self.total_height - self.y*self.height - self.height

    def get_symbol_position(self):
        coord = self.get_box_position()
        return coord[0] + self.width/2 , coord[1] + self.height/2 + self.symbol_size/3

    def get_atomic_number_position(self):
        coord = self.get_box_position()
        return coord[0] + self.stroke_width , coord[1] +  self.stroke_width + self.atomic_number_size*2/3

    def get_atomic_weight_position(self):
        coord = self.get_box_position()
        return coord[0] + self.stroke_width, coord[1] + self.height -  self.stroke_width


    def draw(self, dwg):
        decay_mode = ''
        if len(self.element.decay_modes_and_intensities) > 0:
            for mode in self.element.decay_modes_and_intensities:
                decay_mode += ' ' + str(mode[0].value)

        self.box = dwg.g(id=(self.element.symbol + "-Z" + str(self.element.atomic_number) + "-N" + str(self.element.atomic_weight)), class_=('element_box' + decay_mode))
        rect = dwg.rect(self.get_box_position(), (self.width, self.height), id=(str(self.x) + self.element.symbol), fill=self.fillBox, stroke=self.stroke, stroke_width=self.stroke_width)
        symbol = dwg.text(class_="Symbol",text=self.element.symbol, insert=self.get_symbol_position(), font_size=str(self.symbol_size)+"px", font_family='Arial', text_anchor="middle")
        atomic_weight = dwg.text(class_="N",text=str(self.element.atomic_number), insert=self.get_atomic_number_position(), font_size=str(self.atomic_number_size)+"px", font_family='Arial')
        atomic_number = dwg.text(class_="Z",text=str(self.element.atomic_weight), insert=self.get_atomic_weight_position(), font_size=str(self.atomic_weight_size)+"px", font_family='Arial')


        self.box.add(rect)
        self.box.add(symbol)
        self.box.add(atomic_number)
        self.box.add(atomic_weight)
        dwg.add(self.box)
