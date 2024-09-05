import svgwrite
import textwrap
from dataclasses import dataclass
from typing import Dict

from nucleidechartlib.graphics.element_box import Element_Box
from nucleidechartlib.graphics.nucleide_sect import Nucleide_Sect
from nucleidechartlib.enums import DecayMode
from utils.utils import draw_arrow

@dataclass
class Nucleide_Table:
    id: int
    name: str
    cols: int
    rows: int
    element_boxes: Dict[int, Element_Box]



    def draw(self, filename, config={}, style="None", description={}, legend={}):
        z_text_color = config.get("Table", {}).get("Z color", "darkgrey")
        n_text_color = config.get("Table", {}).get("N color", "darkgrey")
        z_font_size = config.get("Table", {}).get("Z font size", 30)
        n_font_size = config.get("Table", {}).get("N font size", 30)
        size = config.get("Table", {}).get("sizes", {"width": 21000, "height": 29700})
        number_of_divisions = config.get("Table", {}).get("number_of_divisions", 1)
        h_offset = config.get("Table", {}).get("base_h_offset", 0)
        v_offset = config.get("Table", {}).get("base_v_offset", 0)
        v_offsets = config.get("Table", {}).get("div_v_offsets", {40,})
        h_offsets = config.get("Table", {}).get("div_h_offsets", {40,})
        ranges_divisions = config.get("Table", {}).get("div_ranges", ((0, 118),))


        size = (size["width"], size["height"])

        box_width = config.get("Element_Box", {}).get("sizes", {}).get("width", 40)
        box_height = config.get("Element_Box", {}).get("sizes", {}).get("height", 40)


        view_box = "0 0 " +  str(size[0]) + " " + str(size[1])
        dwg = svgwrite.Drawing(filename, size=size, viewBox=view_box)

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
                    section[section_number].add(box.draw(dwg, config))
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
            n = dwg.text(str(col), insert=(x,y), fill=z_text_color, font_size=z_font_size, text_anchor="middle", font_weight="bold")
            for ranges in ranges_divisions:
                if ranges[0] <= columns[col] <= ranges[1]:
                    section_numbers[section_numbers_n].add(n)
                section_numbers_n = section_numbers_n + 1
        for row in rows:
            x = - box_width/2 + rows[row]*box_width
            y = row*box_height + box_width/2 - n_font_size/4
            y = -y
            section_numbers_n = 0
            n = dwg.text(str(row), insert=(x, y), fill=n_text_color, font_size=n_font_size, text_anchor="middle", font_weight="bold")
            for ranges in ranges_divisions:
                if ranges[0] <= row <= ranges[1]:
                    section_numbers[section_numbers_n].add(n)
                section_numbers_n = section_numbers_n + 1




        dwg.add(self.draw_border(dwg, config))

        nucleides.add(boxes)
        nucleides.add(axis)

        dwg.add(nucleides)

        dwg.add(self.draw_legend(dwg, config, legend_description=legend))
        if description != {}:
            dwg.add(self.draw_description(dwg=dwg, config=config, description=description))

        self.draw_title(dwg)
        dwg.add(self.draw_axis(dwg, config))
        dwg.save()
        with open(filename, 'r') as fin:
            data = fin.read().splitlines(True)
        with open(filename, 'w') as fout:
            fout.writelines(data[1:])
        if style != 'None':
            self.set_style(filename, style)


    def draw_border(self, dwg, config={}):
        offset = config.get("Table", {}).get("border_offset", (80, 80))
        size = config.get("Table", {}).get("sizes", {"width": 21000, "height": 29700})
        border_width = config.get("Table", {}).get("border_width", 1)
        border_color = config.get("Table", {}).get("border_color", "black")
        border_background = config.get("Table", {}).get("color", "none")
        rect = dwg.rect(id="border", insert=(offset[0], offset[1]), size=(size["width"]-offset[0]*2, size["height"]-offset[1]*2), fill=border_background, stroke=border_color, stroke_width=border_width)
        return rect

    def draw_legend(self, dwg, config={}, legend_description={}):
        element_box_size = config.get("Element_Box", {}).get("sizes", {"width": 40, "height": 40})
        colors = config.get("colors")
        legend_config = config.get("Legend", {})
        sizes = legend_config.get("sizes", {})
        offset = legend_config.get("offset", (40, 40))
        border_width = legend_config.get("border_width", 1)
        border_color = legend_config.get("border_color", "black")
        panel_background = legend_config.get("panel_background", "none")
        title_font = legend_config.get("title_font", 7)
        title_font_color = legend_config.get("title_font_color", "black")
        title_offset = (0,0)
        title_offset = legend_config.get("title_offset")
        decays_examples_font = legend_config.get("decays_examples_font", 4)
        decays_examples_offset = legend_config.get("decays_examples_offset", (20, 60))
        decays_examples_font_offset = legend_config.get("decays_examples_font_offset", (20, 60))
        decays_examples_font_color = legend_config.get("decays_examples_font_color", "black")
        decays_examples_width = legend_config.get("decays_examples_width", 45)


        sizes = (sizes["width"], sizes["height"])

        legend = dwg.g(id="legend", transform="translate(" + str(offset[0]) + ", " + str(offset[1]) + ")")
        panel = dwg.rect(size=sizes, fill=panel_background, stroke=border_color, stroke_width=border_width, class_="panel")
        title = dwg.text(text="Legend", insert=title_offset, fill=title_font_color, font_size=title_font, text_anchor="middle")

        decay_boxes = dwg.g(id="DecayModes_Legend", transform="translate(" + str(decays_examples_offset[0]) + ", " + str(decays_examples_offset[1]) + ")")

        i = 0
        for decay_mode in DecayMode:
            decay_mode_name = decay_mode.name
            decay_mode_value = decay_mode.value
            decay_mode_color = colors.get("DecayModes", {}).get(decay_mode_name, {}).get("fill", "#FFFFFF")
            decay_mode_text_color = colors.get("DecayModes", {}).get(decay_mode_name, {}).get("text", "#000000")

            group = dwg.g(id=decay_mode_name, transform="translate(0, "+str(i*element_box_size["height"])+")")
            rect = dwg.rect(size=(element_box_size["width"], element_box_size["height"]), class_=decay_mode_name, fill=decay_mode_color)
            border = dwg.rect(size=(element_box_size["width"], element_box_size["height"]), fill="none", stroke=border_color, stroke_width=border_width)
            symbol = dwg.text(text=decay_mode_name[0], insert=(element_box_size["width"]/2, element_box_size["height"]/2+decays_examples_font/4), fill=decay_mode_text_color, font_size=decays_examples_font, text_anchor="middle")

            description = decay_mode_value + ": " + legend_description.get(decay_mode_value, "")
            text = dwg.text(text="", insert=decays_examples_font_offset, fill=decays_examples_font_color, font_size=decays_examples_font)
            if len(description) > decays_examples_width:
                text.add(dwg.tspan(description[0:decays_examples_width], x=[decays_examples_font_offset[0]], dy=[0]))
                for k in range(decays_examples_width, len(description), decays_examples_width):
                    text.add(dwg.tspan(description[k:k+decays_examples_width], x=[decays_examples_font_offset[0]], dy=["1em"]))
            else:
                text.add(dwg.tspan(description, x=[decays_examples_font_offset[0]], dy=[0]))


            group.add(rect)
            group.add(symbol)
            group.add(border)
            group.add(text)



            decay_boxes.add(group)
            i = i + 1

        legend.add(panel)
        legend.add(title)
        legend.add(decay_boxes)

        return legend


    def draw_title(self, dwg):
        x_offset = 90
        y_offset = 180

        dwg.add(dwg.text('Nucleide Chart Generator', insert=(x_offset, y_offset), font_size=100, font_family="Arial", font_weight="bold"))

        y_offset += 50

        font_size = 30
        max_width = 60

        texts = [
            "Generated by: nucleidechart.vaelico.es",
            "Version: 1.0",
            "Author: Alfonso Jesús Piñera Herrera",
            "Email: alfonsojph786@gmail.com",
            "Made in collaboration with: GranaSAT",
            "GranaSAT Location: Av. de Madrid, 28, Beiro, 18012 Granada",
            "GranaSAT Email: granasat@ugr.es",
            "Credits: University of Granada (UGR) - Higher Technical School of Computer Science and Telecommunications Engineering (ETSIIT)",
            "",
            "License:",
            "This work is licensed under a Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0) license."
        ]

        for text in texts:
            # Dividir el texto en varias líneas si excede el ancho máximo
            wrapped_lines = textwrap.wrap(text, width=max_width)
            for line in wrapped_lines:
                dwg.add(dwg.text(line, insert=(x_offset, y_offset), font_size=font_size, font_family="Arial"))
                y_offset += 50  # Ajustar el espacio entre líneas según se desee

    def draw_description(self, dwg, config, description):
        offsets = config.get("Legend", {}).get("description_offset", ((40, 40), (400, 400)))
        font_size = config.get("Legend", {}).get("description_font_size", 15)
        width = config.get("Legend", {}).get("description_width", 80)
        space_between_jumps = config.get("Legend", {}).get("description_space_between_jumps", "1em")
        space_between_lines = config.get("Legend", {}).get("description_space_between_lines", "1.5em")
        font_color = config.get("Legend", {}).get("description_font_color", "black")
        font_family = config.get("Legend", {}).get("description_font_family", "Arial")
        font_weight ="normal"


        description_group = dwg.g(id="description")
        i = 0
        for key in description:
            offset = offsets[i]
            text = dwg.text("", id=("description" + str(i)), insert=(offset[0], offset[1]), fill=font_color, font_size=font_size, font_family=font_family)
            for line in description[key].split("\n"):
                if len(line)<=width:
                    if "**" in line:
                        line = line.replace("**", "")
                        font_weight = "bold"
                    text.add(dwg.tspan(line, x=[offset[0]], dy=[space_between_lines], font_weight=font_weight))
                else:
                    text.add(dwg.tspan(line[0:width], x=[offset[0]], dy=[space_between_lines]))
                    for k in range(width, len(line), width):
                        text.add(dwg.tspan(line[k:k+width], x=[offset[0]], dy=[space_between_jumps]))
            description_group.add(text)
            i+=1


        return description_group

    def draw_axis(self, dwg, config):
        element_box_size = config.get("Element_Box", {}).get("sizes", {"width": 40, "height": 40})
        border_offset = config.get("Table", {}).get("border_offset", (80, 80))
        size = config.get("Table", {}).get("sizes", {"width": 21000, "height": 29700})
        h_offset = border_offset[0] + element_box_size["width"]
        v_offset = size['height'] - border_offset[1] - element_box_size["height"]

        group = dwg.g(id="axis_directions", transform="translate("+str(h_offset)+", "+str(v_offset)+")")
        p_arrow = draw_arrow(dwg, (0, 0), (0, -750), stroke_width=4, stroke_color="black", arrow_size=10)
        n_arrow = draw_arrow(dwg, (0, 0), (750, 0), stroke_width=4, stroke_color="black", arrow_size=10)

        p_text = dwg.text("Z", insert=(45, -100), fill="black", font_size=90, text_anchor="middle")
        n_text = dwg.text("N", insert=(100, -30), fill="black", font_size=90, text_anchor="middle")

        group.add(p_arrow)
        group.add(n_arrow)
        group.add(p_text)
        group.add(n_text)

        return group

    def set_style(self, filename, style):
        style_line = "<?xml-stylesheet type=\"text/css\" href=\"" + style + "\" ?>\n"
        with open(filename, 'r') as file:
            lines = file.readlines()

        if len(lines) > 1:
            lines.insert(1, style_line + '\n')
        else:
            lines.append('\n')
            lines.append(style_line + '\n')

        with open(filename, 'w') as file:
            file.writelines(lines)
