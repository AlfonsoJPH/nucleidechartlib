from ..src.nucleids_chart.element import Element
from ..src.nucleids_chart.csv_driver import read_elements
import unittest

class TestElement(unittest.TestCase):
    def test_element(self):
        element = Element('H', 1, 1.008)
        self.assertEqual(element.symbol, 'H')
        self.assertEqual(element.atomic_number, 1)
        self.assertEqual(element.atomic_weight, 1.008)

    def test_element_invalid_symbol(self):
        with self.assertRaises(ValueError):
            element = Element(1, 1, 1.008)

    def test_bundle_of_elements(self):
        elements = set()
        elements = read_elements("datos.csv")

        print("size is " + str(len(elements)))

        self.assertEqual(len(elements), 5842)
