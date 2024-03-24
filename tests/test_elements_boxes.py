from ..src.nucleids_chart.element import Element
from ..src.nucleids_chart.element_box import ElementBox
import svgwrite
import unittest

class TestElementBox(unittest.TestCase):
    def test_box(self):
        element = Element('H', 1, 1.008)
        box = ElementBox(element, 100, 100, 'black', 10)
        dwg = svgwrite.Drawing('test.svg', profile='tiny')
        box.draw(dwg)
        dwg.save()
