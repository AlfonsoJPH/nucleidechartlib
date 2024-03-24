from ..src.nucleids_chart.element import Element
import unittest

class TestElement(unittest.TestCase):
    def test_element(self):
        element = Element('H', 1, 1.008)
        self.assertEqual(element.symbol, 'H')
        self.assertEqual(element.atomic_number, 1)
        self.assertEqual(element.atomic_weight, 1.008)
