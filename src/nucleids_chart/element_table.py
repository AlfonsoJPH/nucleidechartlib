import svgwrite
from .element_box import ElementBox


class ElementTable:
    def __init__(self, elements):
        self.elements = elements
        self.table = set()
        self.size = (3000, 1250)

        for element in elements:
            self.add_element(element)


    def draw(self, filename):
        dwg = svgwrite.Drawing(filename, profile='tiny', size=self.size)
        for box in self.table:
            box.draw(dwg)
        dwg.save()




    def add_element(self, element):
        box = ElementBox(element, 10, 10, 'beige', 1)
        self.table.add(box)
