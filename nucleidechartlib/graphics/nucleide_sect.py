from dataclasses import dataclass

from nucleidechartlib.enums import DecayMode
from typing import Dict

@dataclass
class Nucleide_Sect:
    id: int
    name: str
    half_life: str
    decay_modes_intensities: Dict[DecayMode, float]
    extra: Dict[DecayMode, float]

    def get_max_decay_mode(self):
        maximum = DecayMode.STABLE

        for key, value in self.decay_modes_intensities.items():
            if (key == DecayMode.STABLE):
                return key
            if value == max(self.decay_modes_intensities.values()):
                maximum = key

        return maximum


    def draw(self, dwg, config={}, total=1):
        if not self.decay_modes_intensities:
            raise ValueError("self.decay_modes_intensities should contain at least one item, element:" + self.name)

        if not all(isinstance(value, (int, float)) for value in self.decay_modes_intensities.values()):
            raise TypeError("All values in self.decay_modes_intensities should be numbers")

        main_decay = self.get_max_decay_mode()

        colors = config.get("colors")
        stroke_color = config.get("colors").get("Stroke")
        stroke_width = config.get("Nucleide_Sect").get("stroke_width")
        border_width = config.get("Nucleide_Sect").get("border_width")
        show_half_life = config.get("Nucleide_Sect").get("show_half_life")
        show_energy = config.get("Nucleide_Sect").get("show_energy")
        size = config.get("Nucleide_Sect").get("sizes")
        element_box_size = config.get("Element_Box").get("sizes")
        half_life_font_size = config.get("Nucleide_Sect", {}).get("sizes", {}).get("half_life_font")
        energy_font_size = config.get("Nucleide_Sect", {}).get("sizes", {}).get("energy_font")

        text_color = "#000000"
        main_color = "#FFFFFF"
        if main_decay:
            main_color = colors.get("DecayModes").get(main_decay.name).get("fill", "#FFFFFF")
            text_color = colors.get("DecayModes").get(main_decay.name).get("text", "#000000")
        else:
            main_color = colors.get("Nucleide_Sect", "#FFFFFF")
            text_color = colors.get("Nucleide_Sect", "#000000")


        x_size = size.get("width")
        y_size = size.get("height")
        x = 0
        y = element_box_size.get("height") - y_size

        if total > 1:
            x = total - 1 - self.id
            x_size = size.get("width", 40) / total
            x = x * x_size


        main_decay_class = " " + main_decay.name
        nucleide_group = dwg.g(id=self.name, class_="nucleide" + main_decay_class, transform="translate(" + str(x) + "," + str(y) + ")")
        rect = dwg.rect(size=(x_size, y_size), class_=('main_decay_mode' + main_decay_class), fill=main_color, stroke=stroke_color, stroke_width=stroke_width)
        nucleide_group.add(rect)

        if True: #config.get("information", {}).get("show_decay_divided", "diagonal") == "diagonal":
            decay_modes = dict(sorted(self.decay_modes_intensities.items(), key=lambda item: item[1], reverse=True))
            # remove the main decay mode
            decay_modes.pop(main_decay)
            i = 0
            for key, value in decay_modes.items():
                actual_color = colors.get("DecayModes").get(key.name).get("fill", "#FFFFFF")
                points = []
                class_ = ''
                if value > 0.05:
                    points = [(x_size,y_size), (0, y_size), (x_size, 0)]
                    class_ = 'other_decay_mode 50%'
                    i += 1
                else:
                    size = max( x_size, y_size)*0.2
                    if size > min(x_size, y_size):
                        size = min(x_size, y_size)

                    if i % 4 == 0:
                        points=[(x_size, y_size), (x_size - size, y_size), (x_size, y_size - size)]

                    elif i % 4 == 1:
                        points=[(0, 0), (size, 0), (0, size)]
                    elif i % 4 == 2:
                        points=[(x_size, 0), (x_size - size, 0), (x_size, size)]
                    else:
                        points=[(0, y_size), (0, y_size - size), (size, y_size)]
                    class_='other_decay_mode 5%'
                    i += 1

                class_ += ' ' + key.name

                triangle = dwg.polygon(points=points, class_=class_, fill=actual_color)

                nucleide_group.add(triangle)

        if show_half_life:
            half_life_font_size = config.get("Nucleide_Sect").get("half_life_font")
            half_life_offset = config.get("Nucleide_Sect").get("half_life_offset")
            half_life_offset = (x_size*half_life_offset[0], half_life_offset[1])

            half_life_text = dwg.text(self.half_life, class_="half_life", insert=half_life_offset, font_size=half_life_font_size, fill=text_color, text_anchor="middle")
            nucleide_group.add(half_life_text)

        if show_energy:
            energy_offset = config.get("Nucleide_Sect").get("energy_offset")
            energy_font_size = config.get("Nucleide_Sect").get("energy_font")

            e = 0
            for key, value in self.extra.items():
                energy_text = dwg.text(key.value + " " + str(value), class_="energy", insert=(energy_offset[0],energy_offset[1]-e*energy_font_size), font_size=energy_font_size, fill=text_color)
                e += 1
                nucleide_group.add(energy_text)



        border = dwg.rect(size=(x_size, y_size), fill="none", stroke=stroke_color, stroke_width=border_width, class_="border")
        nucleide_group.add(border)

        return nucleide_group
