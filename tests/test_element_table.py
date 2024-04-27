from ..src.nucleids_chart.element_table import ElementTable
from ..src.nucleids_chart import csv_driver
import svgwrite
import unittest
import os

class TestElementTable(unittest.TestCase):
    def test_table(self):
        elements = csv_driver.read_elements('datos.csv')
        self.assertTrue(len(elements) > 0)
        table = ElementTable(elements)



        table.draw('test_table.svg')

        self.assertTrue(os.path.exists('test_table.svg'))
        os.execvp('feh', ['feh', 'test_table.svg'])
