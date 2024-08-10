import svgwrite
from dataclasses import dataclass
from typing import Dict

from nucleidechartlib.graphics.element_box import Element_Box
from nucleidechartlib.graphics.nucleide_sect import Nucleide_Sect
from nucleidechartlib.enums import DecayMode
from nucleidechartlib.graphics.config import default_config

@dataclass
class Nucleide_Table:
    id: int
    name: str
    cols: int
    rows: int
    element_boxes: Dict[int, Element_Box]



    def draw(self, filename, config={}, style="None"):
        color = default_config.get("Table", {}).get("color", "#FFFFFF")
        text_color = default_config.get("Table", {}).get("Text", "black")
        z_text_color = default_config.get("Table", {}).get("Z color", "darkgrey")
        n_text_color = default_config.get("Table", {}).get("N color", "darkgrey")
        font_size_1 = default_config.get("Table", {}).get("font1", 30)
        font_size_2 = default_config.get("Table", {}).get("font2", 12)
        font_size_3 = default_config.get("Table", {}).get("font3", 10)
        z_font_size = default_config.get("Table", {}).get("Z font size", 30)
        n_font_size = default_config.get("Table", {}).get("N font size", 30)
        size = default_config.get("Table", {}).get("sizes", {"width": 21000, "height": 29700})
        number_of_divisions = default_config.get("Table", {}).get("number_of_divisions", 1)
        h_offset = default_config.get("Table", {}).get("base_h_offset", 0)
        v_offset = default_config.get("Table", {}).get("base_v_offset", 0)
        v_offsets = default_config.get("Table", {}).get("div_v_offsets", {40,})
        h_offsets = default_config.get("Table", {}).get("div_h_offsets", {40,})
        ranges_divisions = default_config.get("Table", {}).get("div_ranges", ((0, 118),))
        if config != {}:
            color = config.get("Table", {}).get("color", color)
            text_color = config.get("Table", {}).get("Text", text_color)
            z_text_color = config.get("Table", {}).get("Z color", z_text_color)
            n_text_color = config.get("Table", {}).get("N color", n_text_color)
            font_size_1 = config.get("Table", {}).get("font1", font_size_1)
            font_size_2 = config.get("Table", {}).get("font2", font_size_2)
            font_size_3 = config.get("Table", {}).get("font3", font_size_3)
            z_font_size = config.get("Table", {}).get("Z font size", z_font_size)
            n_font_size = config.get("Table", {}).get("N font size", n_font_size)
            size = config.get("Table", {}).get("sizes", size)
            number_of_divisions = config.get("Table", {}).get("number_of_divisions", number_of_divisions)
            h_offset = config.get("Table", {}).get("base_h_offset", h_offset)
            v_offset = config.get("Table", {}).get("base_v_offset", v_offset)
            v_offsets = config.get("Table", {}).get("div_v_offsets", v_offsets)
            h_offsets = config.get("Table", {}).get("div_h_offsets", h_offsets)
            ranges_divisions = config.get("Table", {}).get("div_ranges", ranges_divisions)


        size = (size["width"], size["height"])

        box_width = config.get("Element_Box", {}).get("sizes", {}).get("width", 40)
        box_height = config.get("Element_Box", {}).get("sizes", {}).get("height", 40)


        view_box = "0 0 " + str(size[0]) + " " + str(size[1])
        dwg = svgwrite.Drawing(filename, profile='tiny', size=size, viewBox=view_box)

        columns = {}
        rows = {}


        nucleides = dwg.g(id="nucleides", transform="translate("+str(h_offset)+", "+str(v_offset)+")")
        section = {}
        i = 0
        boxes = dwg.g(id="boxes")
        while i < number_of_divisions:
            actual_range = ranges_divisions[i]
            h_offset = h_offsets[i]
            v_offset = v_offsets[i]

            section[i] = dwg.g(id="section_"+str(i), transform="translate("+str(h_offset - actual_range[0]*box_width)+", "+str(size[1]-(v_offset - actual_range[0]*box_height))+")")
            boxes.add(section[i])
            i = i + 1


        for box in self.element_boxes.values():
            protons = box.atomic_number
            neutrons = box.mass_number - protons

            if neutrons not in columns or protons < columns[neutrons]:
                columns[neutrons] = protons
            if protons not in rows or neutrons < rows[protons]:
                rows[protons] = neutrons

            section_number = 0
            for ranges in ranges_divisions:
                if ranges[0] <= protons <= ranges[1]:
                    section[section_number].add(box.draw(dwg))
                section_number = section_number + 1


        section_numbers = {}
        i = 0
        axis = dwg.g(id="Axis")
        while i < number_of_divisions:
            h_offset = h_offsets[i]
            v_offset = v_offsets[i]
            actual_range = ranges_divisions[i]
            section_numbers[i] = dwg.g(id="section_"+str(i), transform="translate("+str(h_offset - actual_range[0]*box_width)+", "+str(size[1]-(v_offset - actual_range[0]*box_height - box_height))+")")
            axis.add(section_numbers[i])
            i = i + 1

        for col in columns:
            x = col * box_width + box_width/2
            y =  columns[col]*box_width - z_font_size/4 - box_width/2
            y = -y
            section_numbers_n = 0
            n = dwg.add(dwg.text(str(col), insert=(x,y), fill=z_text_color, font_size=z_font_size, text_anchor="middle", font_weight="bold"))
            for ranges in ranges_divisions:
                if ranges[0] <= columns[col] <= ranges[1]:
                    section_numbers[section_numbers_n].add(n)
                section_numbers_n = section_numbers_n + 1
        for row in rows:
            x = - box_width/2 + rows[row]*box_width
            y = row*box_height + box_width/2 - n_font_size/4
            y = -y
            section_numbers_n = 0
            n = dwg.add(dwg.text(str(row), insert=(x, y), fill=n_text_color, font_size=n_font_size, text_anchor="middle", font_weight="bold"))
            for ranges in ranges_divisions:
                if ranges[0] <= row <= ranges[1]:
                    section_numbers[section_numbers_n].add(n)
                section_numbers_n = section_numbers_n + 1




        dwg.add(self.draw_border(dwg, config))

        nucleides.add(boxes)
        nucleides.add(axis)

        dwg.add(nucleides)

        dwg.add(self.draw_legend(dwg, config))

        dwg.save()
        with open(filename, 'r') as fin:
            data = fin.read().splitlines(True)
        with open(filename, 'w') as fout:
            fout.writelines(data[1:])
        if style != 'None':
            self.set_style(filename, style)


    def draw_border(self, dwg, config={}):
        offset = default_config.get("Table", {}).get("border_offset", (80, 80))
        size = default_config.get("Table", {}).get("sizes", {"width": 21000, "height": 29700})
        border_width = default_config.get("Table", {}).get("border_width", 1)
        border_color = default_config.get("Table", {}).get("border_color", "black")
        if config != {}:
            offset = config.get("Table", {}).get("border_offset", offset)
            size = config.get("Table", {}).get("sizes", size)
            border_width = config.get("Table", {}).get("border_width", border_width)
            border_color = config.get("Table", {}).get("border_color", border_color)
        rect = dwg.rect(id="border", insert=(offset[0], offset[1]), size=(size["width"]-offset[0]*2, size["height"]-offset[1]*2), fill="none", stroke=border_color, stroke_width=border_width)
        return rect

    def draw_legend(self, dwg, config):
        element_box_size = default_config.get("Element_Box", {}).get("sizes", {"width": 40, "height": 40})
        colors = default_config.get("colors")
        legend_config = default_config.get("Legend", {})
        sizes = legend_config.get("sizes", {})
        offset = legend_config.get("offset", (40, 40))
        border_width = legend_config.get("border_width", 1)
        border_color = legend_config.get("border_color", "black")
        panel_background = legend_config.get("panel_background", "none")
        show_title = legend_config.get("show_title", True)
        title_font = legend_config.get("title_font", 7)
        title_font_color = legend_config.get("title_font_color", "black")
        title_offset = (0,0)
        title_offset = legend_config.get("title_offset")
        show_decays_examples = legend_config.get("show_decays_examples", True)
        show_decays_examples_text = legend_config.get("show_decays_examples_text", True)
        decays_examples_font = legend_config.get("decays_examples_font", 4)
        decays_examples_offset = legend_config.get("decays_examples_offset", (20, 60))
        decays_examples_font_offset = legend_config.get("decays_examples_font_offset", (20, 60))
        decays_examples_font_color = legend_config.get("decays_examples_font_color", "black")
        show_nucleides_examples = legend_config.get("show_nucleides_examples", True)
        show_nucleides_examples_text = legend_config.get("show_nucleides_examples_text", True)
        nucleides_examples_font = legend_config.get("nucleides_examples_font", 4)
        nucleides_examples_offset = legend_config.get("nucleides_examples_offset", (20, 60))
        nucleides_examples_font_offset = legend_config.get("nucleides_examples_font_offset", (20, 60))
        nucleides_examples_font_color = legend_config.get("nucleides_examples_font_color", "black")
        if config != {}:
            colors = config.get("colors", colors)
            element_box_size = config.get("Element_Box", {}).get("sizes", element_box_size)
            sizes = config.get("Legend", {}).get("sizes", sizes)
            offset = config.get("Legend", {}).get("offset", offset)
            border_width = config.get("Legend", {}).get("border_width", border_width)
            border_color = config.get("Legend", {}).get("border_color", border_color)
            panel_background = config.get("Legend", {}).get("panel_background", panel_background)
            show_title = config.get("Legend", {}).get("show_title", show_title)
            title_font = config.get("Legend", {}).get("title_font", title_font)
            title_font_color = config.get("Legend", {}).get("title_font_color", title_font_color)
            title_offset = config.get("Legend", {}).get("title_offset", title_offset)
            show_decays_examples = config.get("Legend", {}).get("show_decays_examples", show_decays_examples)
            show_decays_examples_text = config.get("Legend", {}).get("show_decays_examples_text", show_decays_examples_text)
            decays_examples_font = config.get("Legend", {}).get("decays_examples_font", decays_examples_font)
            decays_examples_offset = config.get("Legend", {}).get("decays_examples_offset", decays_examples_offset)
            decays_examples_font_offset = config.get("Legend", {}).get("decays_examples_font_offset", decays_examples_font_offset)
            decays_examples_font_color = config.get("Legend", {}).get("decays_examples_font_color", decays_examples_font_color)
            show_nucleides_examples = config.get("Legend", {}).get("show_nucleides_examples", show_nucleides_examples)
            show_nucleides_examples_text = config.get("Legend", {}).get("show_nucleides_examples_text", show_nucleides_examples_text)
            nucleides_examples_font = config.get("Legend", {}).get("nucleides_examples_font", nucleides_examples_font)
            nucleides_examples_offset = config.get("Legend", {}).get("nucleides_examples_offset", nucleides_examples_offset)
            nucleides_examples_font_offset = config.get("Legend", {}).get("nucleides_examples_font_offset", nucleides_examples_font_offset)
            nucleides_examples_font_color = config.get("Legend", {}).get("nucleides_examples_font_color", nucleides_examples_font_color)


        sizes = (sizes["width"], sizes["height"])

        legend = dwg.g(id="legend", transform="translate(" + str(offset[0]) + ", " + str(offset[1]) + ")")
        panel = dwg.rect(size=sizes, fill=panel_background, stroke=border_color, stroke_width=border_width, class_="panel")
        title = dwg.text(text="Leyenda", insert=title_offset, fill=title_font_color, font_size=title_font, text_anchor="middle")

        decay_boxes = dwg.g(id="DecayModes_Legend", transform="translate(" + str(decays_examples_offset[0]) + ", " + str(decays_examples_offset[1]) + ")")

        i = 0
        for decay_mode in DecayMode:
            decay_mode_name = decay_mode.name
            decay_mode_value = decay_mode.value
            decay_mode_color = colors.get("DecayModes", {}).get(decay_mode_name, {}).get("fill", "#FFFFFF")
            decay_mode_text_color = colors.get("DecayModes", {}).get(decay_mode_name, {}).get("text", "#000000")

            group = dwg.g(id=decay_mode_name, transform="translate(0, "+str(i*element_box_size["height"])+")")
            rect = dwg.rect(size=(element_box_size["width"], element_box_size["height"]), class_=decay_mode_name, fill=decay_mode_color)
            symbol = dwg.text(text=decay_mode_name[0], insert=(element_box_size["width"]/2, element_box_size["height"]/2+decays_examples_font/4), fill=decay_mode_text_color, font_size=decays_examples_font, text_anchor="middle")
            text = dwg.text(text=decay_mode_value, insert=decays_examples_font_offset, fill=decays_examples_font_color, font_size=decays_examples_font)

            group.add(rect)
            group.add(symbol)
            group.add(text)

            decay_boxes.add(group)
            i = i + 1

        decays_50 = {}
        decays_50[DecayMode.ALPHA] = 90
        decays_50[DecayMode.BETA_PLUS] = 50
        nucleide_50 = Nucleide_Sect(0, "Nucleide_50", "H U", decays_50, {})

        element_50 = Element_Box(0,"Element","E", 0, 0, {0: nucleide_50})

        i = i + 1

        # group_50 = dwg.g(id="Element_50", transform="translate(0, "+str(i*element_box_size["height"])+")")
        # string_50 = "E es el nombre del elemento que representa, el número que aparece a su derecha es su número atómico y el número que aparece a su izquierda es su número de másico.\nCuando una caja de elemento contiene más de un nucleido, el número de másico y el número atómico se separan por un espacio en blanco.\nEn el caso de que un nucleido tenga más de un modo de desintegración, se muestra el modo de desintegración con mayor intensidad.\nEn el caso de que un nucleido tenga más de un modo de desintegración con la misma intensidad, se muestra el modo de desintegración con menor número atómico.\nEn el caso de que un nucleido tenga más de un modo de desintegración con la misma intensidad y el mismo número atómico, se muestra el modo de desintegración con menor número de másico.\nEn el caso de que un nucleido tenga más de un modo de desintegración, se muestra el modo principal en la zona superior donde aparece el nombre, y dependiendo de la intensidad la caja puede estar dividida a la mitad"
        # text_50 = dwg.text(text=string_50, insert=(element_box_size["width"]/2, element_box_size["height"]/2+font_size_2/2), fill="black", font_size=font_size_2)
        # group_50.add(element_50.draw(dwg))
        # group_50.add(text_50)


        # decay_boxes.add(group_50)

        legend.add(panel)
        legend.add(title)
        legend.add(decay_boxes)

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
