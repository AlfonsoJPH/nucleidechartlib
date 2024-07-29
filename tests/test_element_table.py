from ..nucleidchartlib.graphics.nucleide_sect import Nucleide_Sect
from ..nucleidchartlib.graphics.nucleide_table import Nucleide_Table
from ..nucleidchartlib.graphics.element_box import Element_Box
from ..utils import csv_driver
import unittest
import os
from dataclasses import dataclass
from typing import Dict

class TestElementTable(unittest.TestCase):
    def test_table(self):
        print("Esto es un test")
        elements = csv_driver.read_elements('../data/example.csv')
        self.assertTrue(len(elements) > 0)

        element_boxes = {}
        id = 0
        for element in elements.values():
            n = 0
            nucleide_boxes = {}
            for nucleide in element.nucleides.values():
                nucleide_boxes[n] = Nucleide_Sect(id=n,
                                                  name=element.symbol+str(element.mass_number)+"-"+str(n),
                                                  half_life=nucleide.half_life,
                                                  decay_modes_intensities=nucleide.decay_modes_intensities)
                n+=1

            element_boxes[id] = Element_Box(id=id,
                                           name=element.symbol+str(element.atomic_number),
                                           symbol=element.symbol,
                                           mass_number=element.mass_number,
                                           atomic_number=element.atomic_number,
                                           nucleides=nucleide_boxes)
            id += 1
        table = Nucleide_Table(id=0, name="Tabla de Nucleidos",
                               cols=100, rows=70, element_boxes=element_boxes)



        table.draw('test_table.svg')#, style='../styles/default_style.css')

        print("last id:" + str(id))

        self.assertTrue(id > 5)
        self.assertTrue(os.path.exists('test_table.svg'))
        # os.execvp('inkscape', ['inkscape', 'test_table.svg'])

    # def test_table_divided(self):
    #     elements = csv_driver.read_elements('datos.csv')
    #     self.assertTrue(len(elements) > 0)
    #     table = ElementTable(elements, "A4", 2)



        # table.draw('test_table_divided.svg')

        # self.assertTrue(os.path.exists('test_table_divided.svg'))
        # os.execvp('firefox', ['firefox', 'test_table_divided.svg'])
