from ..nucleidchartlib.graphics.nucleide_sect import Nucleide_Sect
from ..nucleidchartlib.graphics.nucleide_table import Nucleide_Table
from ..nucleidchartlib.graphics.element_box import Element_Box
from ..utils import csv_driver
import unittest
import os
from dataclasses import dataclass
from typing import Dict

def test_table():
    elements = csv_driver.read_elements('../datos.csv')

    element_boxes = {}
    id = 0
    for element in elements.values():
        n = 0
        nucleide_boxes = {}
        for nucleide in element.nucleides.values():
            nucleide_boxes[n] = Nucleide_Sect(id=n,
                                              name=element.symbol+str(n),
                                              half_life=nucleide.half_life,
                                              decay_modes_intensities=nucleide.decay_modes_intensities)

        element_boxes[id] = Element_Box(id=id,
                                       name=element.symbol+str(element.atomic_number),
                                       symbol=element.symbol,
                                       mass_number=element.mass_number,
                                       atomic_number=element.atomic_number,
                                       nucleides=nucleide_boxes)
    table = Nucleide_Table(id=0, name="Tabla de Nucleidos", elements=element_boxes, cols=18, rows=7, element_boxes={})



    table.draw('test_table.svg')


test_table()
