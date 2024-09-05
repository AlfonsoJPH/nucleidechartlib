from nucleidechartlib.graphics.nucleide_sect import Nucleide_Sect
from nucleidechartlib.graphics.nucleide_table import Nucleide_Table
from nucleidechartlib.graphics.element_box import Element_Box
from utils import csv_driver
import unittest
import os

class TestElementTable(unittest.TestCase):
    def test_table(self):
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
                                                  decay_modes_intensities=nucleide.decay_modes_intensities,
                                                  extra={})
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



        table.draw('table_A_landscape_3div_regular.svg')#, style='../styles/default_style.css')

        self.assertTrue(id > 5)
        self.assertTrue(os.path.exists('test_table.svg'))
