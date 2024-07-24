from ..src.nucleids_chart.element_table import ElementTable
from ..src.nucleids_chart import csv_driver
import unittest
import os

class TestElementTable(unittest.TestCase):
    def test_table(self):
        elements = csv_driver.read_elements('datos.csv')
        self.assertTrue(len(elements) > 0)
        table = ElementTable(elements, "A4")



        table.draw('test_table.svg')

        self.assertTrue(os.path.exists('test_table.svg'))
        os.execvp('firefox', ['firefox', 'test_table.svg'])

    def test_table_divided(self):
        elements = csv_driver.read_elements('datos.csv')
        self.assertTrue(len(elements) > 0)
        table = ElementTable(elements, "A4", 2)



        table.draw('test_table_divided.svg')

        self.assertTrue(os.path.exists('test_table_divided.svg'))
        os.execvp('firefox', ['firefox', 'test_table_divided.svg'])
