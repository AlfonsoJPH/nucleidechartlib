import svgwrite
from dataclasses import dataclass
from typing import Dict

from svgwrite.container import ViewBox
from .element_box import Element_Box

size = (7200, 4800)
@dataclass
class Nucleide_Table:
    id: int
    name: str
    cols: int
    rows: int
    element_boxes: Dict[int, Element_Box]



    def draw(self, filename, config={}, style="None"):
        color = config.get("Table", {}).get("color", "#FFFFFF")
        text_color = config.get("Table", {}).get("Text", "black")
        font_size_1 = config.get("Table", {}).get("font1", "30px")
        font_size_2 = config.get("Table", {}).get("font2", "20px")
        font_size_3 = config.get("Table", {}).get("font3", "10px")

        box_width = config.get("Element_Box", {}).get("sizes", {}).get("width", 10)
        box_height = config.get("Element_Box", {}).get("sizes", {}).get("height", 10)


        dwg = svgwrite.Drawing(filename, profile='tiny', size=size, viewBox=("0 0 7200 4800"))
        # dwg.add(self.draw_border(dwg))
        # dwg.add(self.draw_legend(dwg))

        boxes = dwg.g(id="boxes", transform="translate(40, "+str(size[1]-40)+")")

        print ("Creating element boxes")
        i=0
        for box in self.element_boxes.values():
            #save on log file the number of box created
            i = i + 1
            print (f"Creating box {i}")

            boxes.add(box.draw(dwg))

        dwg.add(boxes)

        dwg.save()

        if style != 'None':
            self.set_style(filename, style)


    def draw_border(self, dwg):
        rect = dwg.rect(insert=(10, 10), size=(287, 200), fill="white")
        return rect

    def draw_legend(self, dwg):
        legend = dwg.g(id="legend")
        panel = legend.rect(insert=(287, 20), size="40 60")
        title = legend.text(_class="title", text="Leyenda")
        alpha_rect = legend.rect(rx=5, ry=5, size="2 2", _class="Alpha")
        alpha_text = legend.text(rx=10, ry=5, text="Alpha")
        return legend

    def set_style(self, filename, style):
        style_line = "<?xml-stylesheet type=\"text/css\" href=\"" + style + "\" ?>\n"
        # Leer el contenido del archivo
        with open(filename, 'r') as file:
            lines = file.readlines()

        # Insertar el texto en la segunda línea (índice 1)
        if len(lines) > 1:
            lines.insert(1, style_line + '\n')
        else:
            # Si el archivo tiene menos de dos líneas, añadir la nueva línea
            lines.append('\n')
            lines.append(style_line + '\n')

        # Escribir el contenido de nuevo en el archivo
        with open(filename, 'w') as file:
            file.writelines(lines)
