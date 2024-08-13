from utils.csv_driver import read_elements, read_element
from nucleidechartlib.graphics.nucleide_sect import Nucleide_Sect
from nucleidechartlib.graphics.nucleide_table import Nucleide_Table
from nucleidechartlib.graphics.element_box import Element_Box
import svgwrite


def load_elements_csv(file_name):
    return read_elements(file_name)

def load_element_csv(file_name, n):
    return read_element(file_name, n)

def gen_chart(elements, output, config, style):
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



    table.draw(filename=output, config=config, style=style)

def gen_element(element, output, config):
    nucleide_boxes = {}
    id = 0
    for nucleide in element.nucleides.values():
        nucleide_boxes[id] = Nucleide_Sect(id=id,
                                          name=element.symbol+str(element.mass_number)+"-"+str(id),
                                          half_life=nucleide.half_life,
                                          decay_modes_intensities=nucleide.decay_modes_intensities,
                                          extra={})
        id+=1

    element_box = Element_Box(id=0,
                               name=element.symbol+str(element.atomic_number),
                               symbol=element.symbol,
                               mass_number=element.mass_number,
                               atomic_number=element.atomic_number,
                               nucleides=nucleide_boxes)

    dwg = svgwrite.Drawing(output)


    dwg.add(element_box.draw(dwg, config))
    dwg.save()
