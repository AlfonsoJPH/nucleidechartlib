from svgwrite.utils import FONT_MIMETYPES, font_mimetype
from .element import DecayMode, Element

class ElementBox:
    def __init__(self, element:Element, div=1, rows=1, columns=1):
        self.element = element
        self.box = None

        self.x = int(element.atomic_weight)
        self.y = int(element.atomic_number)
        self.div = div
        self.rows = rows
        self.columns = columns




    def get_position(self):
        x = self.x + 10
        y = 180-self.y

        if self.div > 1:
            if x > self.rows/self.div:
                x = x - (self.rows/self.div) * (x%self.rows)
            if y > self.columns/self.div:
                y = y - (self.columns/self.div) * (y%self.columns)

        return x, y

    def draw(self, dwg):
        decay_mode = ''
        if len(self.element.decay_modes_and_intensities) > 0:
            for mode in self.element.decay_modes_and_intensities:
                decay_mode += ' ' + str(mode[0].value)

        self.box = dwg.g(id=(self.element.symbol + "-Z" + str(self.element.atomic_number) + "-N" + str(self.element.atomic_weight)), class_=('element_box' + decay_mode))
        rect = dwg.rect(self.get_position(), id=(str(self.x) + self.element.symbol))
        symbol = dwg.text(class_="Symbol",text=self.element.symbol, insert=self.get_position(), font_size=1)
        atomic_weight = dwg.text(class_="N",text=str(self.element.atomic_number), insert=self.get_position(), font_size=1)
        atomic_number = dwg.text(class_="Z",text=str(self.element.atomic_weight), insert=self.get_position(), font_size=1)


        self.box.add(rect)
        self.box.add(symbol)
        self.box.add(atomic_number)
        self.box.add(atomic_weight)
        dwg.add(self.box)
