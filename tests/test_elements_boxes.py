from ..src.nucleids_chart.element import DecayMode, Element
from ..src.nucleids_chart.element_box import ElementBox
import svgwrite
import unittest
import os

class TestElementBox(unittest.TestCase):
    def test_box(self):
        element = Element('H', 1, 1)
        element.decay_modes_and_intensities = [(DecayMode.ALPHA, 1)]
        element2 = Element('B', 2, 1)
        element3 = Element('C', 1, 2)
        element4 = Element('N', 4, 4)

        box = ElementBox(element, 100, 100, 'black', 10)
        box2 = ElementBox(element2, 100, 100, 'black', 10)
        box3 = ElementBox(element3, 100, 100, 'black', 10)
        box4 = ElementBox(element4, 100, 100, 'black', 10)
        dwg = svgwrite.Drawing('test_boxes.svg', profile='tiny', size=(1000, 1000))


        box.draw(dwg)
        box2.draw(dwg)
        box3.draw(dwg)
        box4.draw(dwg)
        dwg.save()

        self.assertTrue(os.path.exists('test_boxes.svg'))
        os.execvp('inkscape', ['inkscape', 'test_boxes.svg'])
