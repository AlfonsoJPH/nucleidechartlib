from dataclasses import dataclass
from typing import Dict

from .nucleide_sect import Nucleide_Sect
from .config import default_config


@dataclass
class Element_Box:
    id: int
    name: str
    symbol: str
    mass_number: float
    atomic_number: int
    nucleides: Dict[int, Nucleide_Sect]

    def get_position(self, config):

        protons = self.atomic_number
        neutrons = self.mass_number - protons

        x = neutrons
        y = protons

        max_cols = config.get("max_cols", 999999)
        if neutrons > max_cols:
            x = x % max_cols
            y = y + (-1)^(protons / max_cols) * max_cols * x / max_cols

        y = y * (-1)

        x = x * config.get("cell_sizes", {"width": 40, "height": 40}).get("width", 40)
        y = y * config.get("cell_sizes", {"width": 40, "height": 40}).get("height", 40)

        return (x, y)


    def draw(self, dwg, config={}):
        colors = default_config.get("colors")
        stroke_color = default_config.get("colors").get("Stroke")
        stroke_width = default_config.get("Element_Box").get("stroke_width")
        border_width = default_config.get("Element_Box").get("border_width")
        font_size = default_config.get("Element_Box").get("font1")
        size = default_config.get("Element_Box").get("sizes")
        if config != {}:
            colors = config.get("colors", colors)
            stroke_color = config.get("colors", {}).get("Stroke", stroke_color)
            stroke_width = config.get("Element_Box", {}).get("sizes", {}).get("stroke_width", stroke_width)
            border_width = config.get("Element_Box", {}).get("sizes", {}).get("border_width", border_width)
            font_size = config.get("Element_Box", {}).get("sizes", {}).get("font1", font_size)
            size = config.get("Element_Box", {}).get("sizes", size)




        #posicion relativa y al final tranform a get_position
        pos = "translate" + str(self.get_position(config))
        main_nucleide = self.nucleides.get(0)
        text_color = "#000000"
        color = "#FFFFFF"
        if main_nucleide:
            print(main_nucleide.get_max_decay_mode())
            color = colors.get("DecayModes").get(main_nucleide.get_max_decay_mode().name).get("fill", "#FFFFFF")
            text_color = colors.get("DecayModes").get(main_nucleide.get_max_decay_mode().name).get("text", "#000000")

        else:
            color = colors.get("Element_Box", "#FFFFFF")
            text_color = colors.get("Element_Box", "#000000")

        class_ = ""
        if main_nucleide:
            class_ = " " + main_nucleide.get_max_decay_mode().name
        box = dwg.g(id=(self.symbol + str(self.mass_number)), class_="element_box" + class_, transform=pos)
        rect = dwg.rect(size=(size["width"], size["height"]), fill=color, stroke=stroke_color, stroke_width=stroke_width, class_="box")
        symbol_text = self.symbol + " " + str(self.mass_number)
        symbol = dwg.text(symbol_text, insert=(stroke_width+(size["width"]/2), stroke_width + font_size), font_size=font_size, fill=text_color, text_anchor="middle")


        box.add(rect)

        for nucleide in self.nucleides.items():
            box.add(nucleide[1].draw(dwg, config, self.nucleides.__len__()))
        box.add(symbol)
        border = dwg.rect(size=(size["width"], size["height"]), fill="none", stroke=stroke_color, stroke_width=border_width, class_="border")
        box.add(border)

        print(self.id)
        return box
