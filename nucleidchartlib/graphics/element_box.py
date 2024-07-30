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

        x = x * config.get("width", 40)
        y = y * config.get("height", 40)

        return (x, y)


    def draw(self, dwg, config={}):
        colors = default_config.get("colors")
        stroke_color = default_config.get("colors").get("Stroke")
        stroke_width = default_config.get("Element_Box").get("stroke_width")
        border_width = default_config.get("Element_Box").get("border_width")
        font_size = default_config.get("Element_Box").get("name_font")
        size = default_config.get("Element_Box").get("sizes")
        max_number_of_nucleides = default_config.get("Element_Box").get("max_number_of_nucleides")
        symbol_and_weight = default_config.get("Element_Box").get("symbol_and_weight")
        if config != {}:
            colors = config.get("colors", colors)
            stroke_color = config.get("colors", {}).get("Stroke", stroke_color)
            stroke_width = config.get("Element_Box", {}).get("sizes", {}).get("stroke_width", stroke_width)
            border_width = config.get("Element_Box", {}).get("sizes", {}).get("border_width", border_width)
            font_size = config.get("Element_Box", {}).get("sizes", {}).get("name", font_size)
            size = config.get("Element_Box", {}).get("sizes", size)
            max_number_of_nucleides = config.get("Element_Box", {}).get("max_number_of_nucleides", max_number_of_nucleides)
            symbol_and_weight = config.get("Element_Box", {}).get("symbol_and_weight", symbol_and_weight)




        #posicion relativa y al final tranform a get_position
        pos = "translate" + str(self.get_position(size))
        main_nucleide = self.nucleides.get(0)
        text_color = "#000000"
        color = "#FFFFFF"
        if main_nucleide:
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
        box.add(rect)

        # plot nucleides

        i = 0
        max_number_of_nucleides = min(max_number_of_nucleides, self.nucleides.__len__())
        for nucleide in self.nucleides.items():
            if i < max_number_of_nucleides:
                box.add(nucleide[1].draw(dwg, config, max_number_of_nucleides))
            i += 1

        # plot symbol and weight
        if symbol_and_weight:
            name_text = self.symbol + " " + str(self.mass_number)

            name_offset = default_config.get("Element_Box").get("name_offset")
            name_font = default_config.get("Element_Box").get("name_font")
            if config != {}:
                name_offset = config.get("Element_Box").get("name_offset", name_offset)
                name_font = config.get("Element_Box").get("name_font", name_font)

            symbol = dwg.text(name_text, insert=name_offset, font_size=name_font, fill=text_color, text_anchor="middle", class_="name")
            box.add(symbol)
        else:
            show_symbol = default_config.get("Element_Box").get("show_symbol")
            if config != {}:
                show_symbol = config.get("Element_Box").get("show_symbol", show_symbol)
            if show_symbol:
                symbol_text = self.symbol

                symbol_font = default_config.get("Element_Box").get("symbol_font")
                symbol_offset = default_config.get("Element_Box").get("symbol_offset")
                if config != {}:
                    symbol_font = config.get("Element_Box").get("symbol_font", symbol_font)
                    symbol_offset = config.get("Element_Box").get("symbol_offset", symbol_offset)
                symbol = dwg.text(symbol_text, insert=symbol_offset, font_size=symbol_font, fill=text_color, text_anchor="middle", class_="symbol")
                box.add(symbol)
            show_weight = default_config.get("Element_Box").get("show_weight")
            if config != {}:
                show_weight = config.get("Element_Box").get("show_weight", show_weight)
            if show_weight:
                weight_text = str(self.mass_number)

                weight_font = default_config.get("Element_Box").get("weight_font")
                weight_offset = default_config.get("Element_Box").get("weight_offset")
                if config != {}:
                    weight_font = config.get("Element_Box").get("weight_font", weight_font)
                    weight_offset = config.get("Element_Box").get("weight_offset", weight_offset)
                weight = dwg.text(weight_text, insert=weight_offset, font_size=weight_font, fill=text_color, text_anchor="middle", class_="weight")
                box.add(weight)



        border = dwg.rect(size=(size["width"], size["height"]), fill="none", stroke=stroke_color, stroke_width=border_width, class_="border")
        box.add(border)

        return box
