import json
unit = 40;
a_base = (2.97, 2.1)
example_config = {
    "Table": {
        "color": "#FFFFFF",
        "Text": "black",
        "Z color": "darkgrey",
        "N color": "darkgrey",
        "font1": 3/4*unit,
        "font2": 1/2*unit,
        "font3": 1/4*unit,
        "Z font size": unit/2,
        "N font size": unit/2,
        "sizes": { "width": a_base[0]*1680 , "height": a_base[1]*1680},
        "border_offset": (unit*2, unit*2),
        "border_width": 1,
        "border_color": "black",
        "base_h_offset": 3.5*unit,
        "base_v_offset": -16*unit,
        "number_of_divisions": 2,
        "div_h_offsets": ( 3*unit, 3*unit - 5 * unit),
        "div_v_offsets": ( unit*8, unit*8-15*unit ),
        "div_ranges": ( (0, 58), (59, 118) ),
    },
    "Element_Box": {
        "sizes": {
            "width": unit,
            "height": unit
        },
        "stroke_width": 0,
        "border_width": 1,
        "max_number_of_nucleides": 3,
        "symbol_and_weight": True,
        #if symbol_and_weight is True, the following parameters are used
        "name": True,
        "name_font": 7,
        "name_offset": (unit/2, 8),
        #if symbol_and_weight is False, the following parameters are used
        "show_symbol": True,
        "show_weight": True,
        "symbol_font": 7,
        "weight_font": 7,
        "symbol_offset": (unit/2, 0),
        "weight_offset": (unit/2, unit/2),
    },
    "Nucleide_Sect": {
        "sizes": {
            "width": unit,
            "height": unit*3/4
        },
        "stroke_width": 0,
        "border_width": 0.2,
        "show_half_life": True,
        "half_life_font": 4,
        "half_life_offset": (1/2, 4),
        "show_energy": True,
        "energy_font": 4,
        "energy_offset": (0, unit),

    },
    "Legend": {
        "sizes": {
            "width": 8*unit,
            "height": 12*unit
        },
        "offset": (2*unit, 2*unit),
        "stroke_width": 0,
        "border_width": 1,
        "border_color": "black",
        "panel_background": "none",
        "show_title": True,
        "title_font": 18,
        "title_font_color": "black",
        "title_offset": (8*unit/2, unit),
        "show_decays_examples": True,
        "show_decays_examples_text": True,
        "decays_examples_font": 10,
        "decays_examples_offset": (unit/2, unit+unit/2),
        "decays_examples_font_offset": (unit/2+unit, unit/2+2.5),
        "decays_examples_font_color": "black",
        "show_nucleides_examples": True,
        "show_nucleides_examples_text": True,
        "nucleides_examples_font": 10,
        "nucleides_examples_offset": (unit/2, unit+10*unit+unit/2),
        "nucleides_examples_font_offset": (unit/2+unit, 10*unit+unit/2+2.5),
        "nucleides_examples_font_color": "black",
    },
    "colors": {
        "Stroke": "black",
        "Element_Box": "#FFFFFF",
        "Nucleide_Sect": "#FFFFFF",
        "DecayModes": {
            "ALPHA": {
                "fill": "#B3A60A",
                "text": "black"
            },
            "BETA_MINUS": {
                "fill": "#548088",
                "text": "black"
            },
            "STABLE": {
                "fill": "black",
                "text": "white"
            },
            "NEUTRON": {
                "fill": "#DC5FCD",
                "text": "black"
            },
            "SF": {
                "fill": "#295F2D",
                "text": "black"
            },
            "BETA_PLUS": {
                "fill": "#AF5E5B",
                "text": "black"
            },
            "IT": {
                "fill": "#C1BAB4",
                "text": "black"
            },
            "ELECTRON_CAPTURE": {
                "fill": "#646293",
                "text": "black"
            },
            "NEUTRON": {
                "fill": "#869898",
                "text": "black"
            }
        }
    },
}

unit = 40;
#A size
A_regular_detail_nodiv_config = {
    "Table": {
        "color": "#FFFFFF",
        "Text": "black",
        "Z color": "darkgrey",
        "N color": "darkgrey",
        "font1": 3/4*unit,
        "font2": 1/2*unit,
        "font3": 1/4*unit,
        "Z font size": unit/2,
        "N font size": unit/2,
        "sizes": { "width": a_base[0]*2600 , "height": a_base[1]*2600},
        "border_offset": (unit*2, unit*2),
        "border_width": 1,
        "border_color": "black",
        "base_h_offset": 3.5*unit,
        "base_v_offset": -1*unit,
        "number_of_divisions": 1,
        "div_h_offsets": ( 3*unit, ),
        "div_v_offsets": ( unit*8,  ),
        "div_ranges": ( (0, 118), ),
    },
    "Element_Box": {
        "sizes": {
            "width": unit,
            "height": unit
        },
        "stroke_width": 0,
        "border_width": 1,
        "max_number_of_nucleides": 3,
        "symbol_and_weight": True,
        #if symbol_and_weight is True, the following parameters are used
        "name": True,
        "name_font": 7,
        "name_offset": (unit/2, 8),
        #if symbol_and_weight is False, the following parameters are used
        "show_symbol": True,
        "show_weight": True,
        "symbol_font": 7,
        "weight_font": 7,
        "symbol_offset": (unit/2, 0),
        "weight_offset": (unit/2, unit/2),
    },
    "Nucleide_Sect": {
        "sizes": {
            "width": unit,
            "height": unit*3/4
        },
        "stroke_width": 0,
        "border_width": 0.2,
        "show_half_life": True,
        "half_life_font": 4,
        "half_life_offset": (1/2, 4),
        "show_energy": True,
        "energy_font": 4,
        "energy_offset": (0, unit),

    },
    "Legend": {
        "sizes": {
            "width": 8*unit,
            "height": 12*unit
        },
        "offset": (2*unit, 2*unit),
        "stroke_width": 0,
        "border_width": 1,
        "border_color": "black",
        "panel_background": "none",
        "show_title": True,
        "title_font": 18,
        "title_font_color": "black",
        "title_offset": (8*unit/2, unit),
        "show_decays_examples": True,
        "show_decays_examples_text": True,
        "decays_examples_font": 10,
        "decays_examples_offset": (unit/2, unit+unit/2),
        "decays_examples_font_offset": (unit/2+unit, unit/2+2.5),
        "decays_examples_font_color": "black",
        "show_nucleides_examples": True,
        "show_nucleides_examples_text": True,
        "nucleides_examples_font": 10,
        "nucleides_examples_offset": (unit/2, unit+10*unit+unit/2),
        "nucleides_examples_font_offset": (unit/2+unit, 10*unit+unit/2+2.5),
        "nucleides_examples_font_color": "black",
        "description_offset": ((40, 40), (400, 400)),
        "description_font_size": 15,
        "description_width": 80,
        "description_space_between_jumps": "1em",
        "description_space_between_lines": "1.5em",
        "description_font_color": "black",
        "description_font_family": "Arial",
    },
    "colors": {
        "Stroke": "black",
        "Element_Box": "#FFFFFF",
        "Nucleide_Sect": "#FFFFFF",
        "DecayModes": {
            "ALPHA": {
                "fill": "#B3A60A",
                "text": "black"
            },
            "BETA_MINUS": {
                "fill": "#548088",
                "text": "black"
            },
            "STABLE": {
                "fill": "black",
                "text": "white"
            },
            "PROTON": {
                "fill": "#AD8516",
                "text": "black"
            },
            "SF": {
                "fill": "#295F2D",
                "text": "black"
            },
            "BETA_PLUS": {
                "fill": "#AF5E5B",
                "text": "black"
            },
            "IT": {
                "fill": "#C1BAB4",
                "text": "black"
            },
            "ELECTRON_CAPTURE": {
                "fill": "#646293",
                "text": "black"
            },
            "NEUTRON": {
                "fill": "#869898",
                "text": "black"
            }
        }
    },
}
A_min_detail_nodiv_config = {
    "Table": {
        "color": "#FFFFFF",
        "Text": "black",
        "Z color": "darkgrey",
        "N color": "darkgrey",
        "font1": 3/4*unit,
        "font2": 1/2*unit,
        "font3": 1/4*unit,
        "Z font size": unit/2,
        "N font size": unit/2,
        "sizes": { "width": a_base[0]*2600 , "height": a_base[1]*2600},
        "border_offset": (unit*2, unit*2),
        "border_width": 1,
        "border_color": "black",
        "base_h_offset": 4*unit,
        "base_v_offset": -1*unit,
        "number_of_divisions": 1,
        "div_h_offsets": ( 3*unit, ),
        "div_v_offsets": ( unit*8,  ),
        "div_ranges": ( (0, 118), ),
    },
    "Element_Box": {
        "sizes": {
            "width": unit,
            "height": unit
        },
        "stroke_width": 0,
        "border_width": 1,
        "max_number_of_nucleides": 0,
        "symbol_and_weight": False,
        #if symbol_and_weight is True, the following parameters are used
        "name": True,
        "name_font": 7,
        "name_offset": (unit/2, unit/2),
        #if symbol_and_weight is False, the following parameters are used
        "show_symbol": True,
        "show_weight": True,
        "symbol_font": 18,
        "weight_font": 10,
        "symbol_offset": (unit/2, unit/2+2),
        "weight_offset": (unit/2, unit -4),
    },
    "Nucleide_Sect": {
        "sizes": {
            "width": unit,
            "height": unit*3/4
        },
        "stroke_width": 0,
        "border_width": 0.2,
        "show_half_life": True,
        "half_life_font": 4,
        "half_life_offset": (1/2, 4),
        "show_energy": True,
        "energy_font": 4,
        "energy_offset": (0, unit),

    },
    "Legend": {
        "sizes": {
            "width": 8*unit,
            "height": 12*unit
        },
        "offset": (2*unit, 2*unit),
        "stroke_width": 0,
        "border_width": 1,
        "border_color": "black",
        "panel_background": "none",
        "show_title": True,
        "title_font": 18,
        "title_font_color": "black",
        "title_offset": (8*unit/2, unit),
        "show_decays_examples": True,
        "show_decays_examples_text": True,
        "decays_examples_font": 10,
        "decays_examples_offset": (unit/2, unit+unit/2),
        "decays_examples_font_offset": (unit/2+unit, unit/2+2.5),
        "decays_examples_font_color": "black",
        "show_nucleides_examples": True,
        "show_nucleides_examples_text": True,
        "nucleides_examples_font": 10,
        "nucleides_examples_offset": (unit/2, unit+10*unit+unit/2),
        "nucleides_examples_font_offset": (unit/2+unit, 10*unit+unit/2+2.5),
        "nucleides_examples_font_color": "black",
    },


    "colors": {
        "Stroke": "black",
        "Element_Box": "#FFFFFF",
        "Nucleide_Sect": "#FFFFFF",
        "DecayModes": {
            "ALPHA": {
                "fill": "#B3A60A",
                "text": "black"
            },
            "BETA_MINUS": {
                "fill": "#548088",
                "text": "black"
            },
            "STABLE": {
                "fill": "black",
                "text": "white"
            },
            "PROTON": {
                "fill": "#AD8516",
                "text": "black"
            },
            "SF": {
                "fill": "#295F2D",
                "text": "black"
            },
            "BETA_PLUS": {
                "fill": "#AF5E5B",
                "text": "black"
            },
            "IT": {
                "fill": "#C1BAB4",
                "text": "black"
            },
            "ELECTRON_CAPTURE": {
                "fill": "#646293",
                "text": "black"
            },
            "NEUTRON": {
                "fill": "#869898",
                "text": "black"
            }
        }
    },
}
A_regular_detail_2div_config = {
    "Table": {
        "color": "#FFFFFF",
        "Text": "black",
        "Z color": "darkgrey",
        "N color": "darkgrey",
        "font1": 3/4*unit,
        "font2": 1/2*unit,
        "font3": 1/4*unit,
        "Z font size": unit/2,
        "N font size": unit/2,
        "sizes": { "width": a_base[0]*1680 , "height": a_base[1]*1680},
        "border_offset": (unit*2, unit*2),
        "border_width": 1,
        "border_color": "black",
        "base_h_offset": 3.5*unit,
        "base_v_offset": -16*unit,
        "number_of_divisions": 2,
        "div_h_offsets": ( 3*unit, 3*unit - 5 * unit),
        "div_v_offsets": ( unit*8, unit*8-15*unit ),
        "div_ranges": ( (0, 58), (59, 118) ),
    },
    "Element_Box": {
        "sizes": {
            "width": unit,
            "height": unit
        },
        "stroke_width": 0,
        "border_width": 1,
        "max_number_of_nucleides": 3,
        "symbol_and_weight": True,
        #if symbol_and_weight is True, the following parameters are used
        "name": True,
        "name_font": 7,
        "name_offset": (unit/2, 8),
        #if symbol_and_weight is False, the following parameters are used
        "show_symbol": True,
        "show_weight": True,
        "symbol_font": 7,
        "weight_font": 7,
        "symbol_offset": (unit/2, 0),
        "weight_offset": (unit/2, unit/2),
    },
    "Nucleide_Sect": {
        "sizes": {
            "width": unit,
            "height": unit*3/4
        },
        "stroke_width": 0,
        "border_width": 0.2,
        "show_half_life": True,
        "half_life_font": 4,
        "half_life_offset": (1/2, 4),
        "show_energy": True,
        "energy_font": 4,
        "energy_offset": (0, unit),

    },
    "Legend": {
        "sizes": {
            "width": 8*unit,
            "height": 12*unit
        },
        "offset": (2*unit, 2*unit),
        "stroke_width": 0,
        "border_width": 1,
        "border_color": "black",
        "panel_background": "none",
        "show_title": True,
        "title_font": 18,
        "title_font_color": "black",
        "title_offset": (8*unit/2, unit),
        "show_decays_examples": True,
        "show_decays_examples_text": True,
        "decays_examples_font": 10,
        "decays_examples_offset": (unit/2, unit+unit/2),
        "decays_examples_font_offset": (unit/2+unit, unit/2+2.5),
        "decays_examples_font_color": "black",
        "show_nucleides_examples": True,
        "show_nucleides_examples_text": True,
        "nucleides_examples_font": 10,
        "nucleides_examples_offset": (unit/2, unit+10*unit+unit/2),
        "nucleides_examples_font_offset": (unit/2+unit, 10*unit+unit/2+2.5),
        "nucleides_examples_font_color": "black",
    },
    "colors": {
        "Stroke": "black",
        "Element_Box": "#FFFFFF",
        "Nucleide_Sect": "#FFFFFF",
        "DecayModes": {
            "ALPHA": {
                "fill": "#B3A60A",
                "text": "black"
            },
            "BETA_MINUS": {
                "fill": "#548088",
                "text": "black"
            },
            "STABLE": {
                "fill": "black",
                "text": "white"
            },
            "PROTON": {
                "fill": "#AD8516",
                "text": "black"
            },
            "SF": {
                "fill": "#295F2D",
                "text": "black"
            },
            "BETA_PLUS": {
                "fill": "#AF5E5B",
                "text": "black"
            },
            "IT": {
                "fill": "#C1BAB4",
                "text": "black"
            },
            "ELECTRON_CAPTURE": {
                "fill": "#646293",
                "text": "black"
            },
            "NEUTRON": {
                "fill": "#869898",
                "text": "black"
            }
        }
    },
}
A_min_detail_2div_config = {
    "Table": {
        "color": "#FFFFFF",
        "Text": "black",
        "Z color": "darkgrey",
        "N color": "darkgrey",
        "font1": 3/4*unit,
        "font2": 1/2*unit,
        "font3": 1/4*unit,
        "Z font size": unit/2,
        "N font size": unit/2,
        "sizes": { "width": a_base[0]*1680 , "height": a_base[1]*1680},
        "border_offset": (unit*2, unit*2),
        "border_width": 1,
        "border_color": "black",
        "base_h_offset": 3*unit,
        "base_v_offset": -18*unit,
        "number_of_divisions": 2,
        "div_h_offsets": ( 3*unit, 3*unit - 5 * unit),
        "div_v_offsets": ( unit*8, unit*3-15*unit ),
        "div_ranges": ( (0, 58), (59, 118) ),
    },
    "Element_Box": {
        "sizes": {
            "width": unit,
            "height": unit
        },
        "stroke_width": 0,
        "border_width": 1,
        "max_number_of_nucleides": 0,
        "symbol_and_weight": False,
        #if symbol_and_weight is True, the following parameters are used
        "name": True,
        "name_font": 7,
        "name_offset": (unit/2, unit/2),
        #if symbol_and_weight is False, the following parameters are used
        "show_symbol": True,
        "show_weight": True,
        "symbol_font": 18,
        "weight_font": 10,
        "symbol_offset": (unit/2, unit/2+2),
        "weight_offset": (unit/2, unit -4),
    },
    "Nucleide_Sect": {
        "sizes": {
            "width": unit,
            "height": unit*3/4
        },
        "stroke_width": 0,
        "border_width": 0.2,
        "show_half_life": True,
        "half_life_font": 4,
        "half_life_offset": (1/2, 4),
        "show_energy": True,
        "energy_font": 4,
        "energy_offset": (0, unit),

    },
    "Legend": {
        "sizes": {
            "width": 8*unit,
            "height": 12*unit
        },
        "offset": (2*unit, 2*unit),
        "stroke_width": 0,
        "border_width": 1,
        "border_color": "black",
        "panel_background": "none",
        "show_title": True,
        "title_font": 18,
        "title_font_color": "black",
        "title_offset": (8*unit/2, unit),
        "show_decays_examples": True,
        "show_decays_examples_text": True,
        "decays_examples_font": 10,
        "decays_examples_offset": (unit/2, unit+unit/2),
        "decays_examples_font_offset": (unit/2+unit, unit/2+2.5),
        "decays_examples_font_color": "black",
        "show_nucleides_examples": True,
        "show_nucleides_examples_text": True,
        "nucleides_examples_font": 10,
        "nucleides_examples_offset": (unit/2, unit+10*unit+unit/2),
        "nucleides_examples_font_offset": (unit/2+unit, 10*unit+unit/2+2.5),
        "nucleides_examples_font_color": "black",
    },


    "colors": {
        "Stroke": "black",
        "Element_Box": "#FFFFFF",
        "Nucleide_Sect": "#FFFFFF",
        "DecayModes": {
            "ALPHA": {
                "fill": "#B3A60A",
                "text": "black"
            },
            "BETA_MINUS": {
                "fill": "#548088",
                "text": "black"
            },
            "STABLE": {
                "fill": "black",
                "text": "white"
            },
            "PROTON": {
                "fill": "#AD8516",
                "text": "black"
            },
            "SF": {
                "fill": "#295F2D",
                "text": "black"
            },
            "BETA_PLUS": {
                "fill": "#AF5E5B",
                "text": "black"
            },
            "IT": {
                "fill": "#C1BAB4",
                "text": "black"
            },
            "ELECTRON_CAPTURE": {
                "fill": "#646293",
                "text": "black"
            },
            "NEUTRON": {
                "fill": "#869898",
                "text": "black"
            }
        }
    },
}



A_regular_detail_3div_config = {
    "Table": {
        "color": "#FFFFFF",
        "Text": "black",
        "Z color": "darkgrey",
        "N color": "darkgrey",
        "font1": 3/4*unit,
        "font2": 1/2*unit,
        "font3": 1/4*unit,
        "Z font size": unit/2,
        "N font size": unit/2,
        "sizes": { "width": a_base[0]*1480 , "height": a_base[1]*1480},
        "border_offset": (unit*2, unit*2),
        "border_width": 1,
        "border_color": "black",
        "base_h_offset": 3*unit,
        "base_v_offset": -26*unit,
        "number_of_divisions": 3,
        "div_h_offsets": ( 3*unit, 3*unit + 7 * unit, 3*unit  ),
        "div_v_offsets": ( unit*8, unit*3-8*unit, unit*3-23*unit),
        "div_ranges": ( (0, 39), (40, 78), (79, 118) ),
    },
    "Element_Box": {
        "sizes": {
            "width": unit,
            "height": unit
        },
        "stroke_width": 0,
        "border_width": 1,
        "max_number_of_nucleides": 3,
        "symbol_and_weight": True,
        #if symbol_and_weight is True, the following parameters are used
        "name": True,
        "name_font": 7,
        "name_offset": (unit/2, 8),
        #if symbol_and_weight is False, the following parameters are used
        "show_symbol": True,
        "show_weight": True,
        "symbol_font": 7,
        "weight_font": 7,
        "symbol_offset": (unit/2, 0),
        "weight_offset": (unit/2, unit/2),
    },
    "Nucleide_Sect": {
        "sizes": {
            "width": unit,
            "height": unit*3/4
        },
        "stroke_width": 0,
        "border_width": 0.2,
        "show_half_life": True,
        "half_life_font": 4,
        "half_life_offset": (1/2, 4),
        "show_energy": True,
        "energy_font": 4,
        "energy_offset": (0, unit),

    },
    "Legend": {
        "sizes": {
            "width": 8*unit,
            "height": 12*unit
        },
        "offset": (2*unit, 2*unit),
        "stroke_width": 0,
        "border_width": 1,
        "border_color": "black",
        "panel_background": "none",
        "show_title": True,
        "title_font": 18,
        "title_font_color": "black",
        "title_offset": (8*unit/2, unit),
        "show_decays_examples": True,
        "show_decays_examples_text": True,
        "decays_examples_font": 10,
        "decays_examples_offset": (unit/2, unit+unit/2),
        "decays_examples_font_offset": (unit/2+unit, unit/2+2.5),
        "decays_examples_font_color": "black",
        "show_nucleides_examples": True,
        "show_nucleides_examples_text": True,
        "nucleides_examples_font": 10,
        "nucleides_examples_offset": (unit/2, unit+10*unit+unit/2),
        "nucleides_examples_font_offset": (unit/2+unit, 10*unit+unit/2+2.5),
        "nucleides_examples_font_color": "black",
    },
    "colors": {
        "Stroke": "black",
        "Element_Box": "#FFFFFF",
        "Nucleide_Sect": "#FFFFFF",
        "DecayModes": {
            "ALPHA": {
                "fill": "#B3A60A",
                "text": "black"
            },
            "BETA_MINUS": {
                "fill": "#548088",
                "text": "black"
            },
            "STABLE": {
                "fill": "black",
                "text": "white"
            },
            "PROTON": {
                "fill": "#AD8516",
                "text": "black"
            },
            "SF": {
                "fill": "#295F2D",
                "text": "black"
            },
            "BETA_PLUS": {
                "fill": "#AF5E5B",
                "text": "black"
            },
            "IT": {
                "fill": "#C1BAB4",
                "text": "black"
            },
            "ELECTRON_CAPTURE": {
                "fill": "#646293",
                "text": "black"
            },
            "NEUTRON": {
                "fill": "#869898",
                "text": "black"
            }
        }
    },
}
A_min_detail_3div_config = {
    "Table": {
        "color": "#FFFFFF",
        "Text": "black",
        "Z color": "darkgrey",
        "N color": "darkgrey",
        "font1": 3/4*unit,
        "font2": 1/2*unit,
        "font3": 1/4*unit,
        "Z font size": unit/2,
        "N font size": unit/2,
        "sizes": { "width": a_base[0]*1480 , "height": a_base[1]*1480},
        "border_offset": (unit*2, unit*2),
        "border_width": 1,
        "border_color": "black",
        "base_h_offset": 3*unit,
        "base_v_offset": -26*unit,
        "number_of_divisions": 3,
        "div_h_offsets": ( 3*unit, 3*unit + 7 * unit, 3*unit  ),
        "div_v_offsets": ( unit*8, unit*3-8*unit, unit*3-23*unit),
        "div_ranges": ( (0, 39), (40, 78), (79, 118) ),
    },
    "Element_Box": {
        "sizes": {
            "width": unit,
            "height": unit
        },
        "stroke_width": 0,
        "border_width": 1,
        "max_number_of_nucleides": 0,
        "symbol_and_weight": False,
        #if symbol_and_weight is True, the following parameters are used
        "name": True,
        "name_font": 7,
        "name_offset": (unit/2, unit/2),
        #if symbol_and_weight is False, the following parameters are used
        "show_symbol": True,
        "show_weight": True,
        "symbol_font": 18,
        "weight_font": 10,
        "symbol_offset": (unit/2, unit/2+2),
        "weight_offset": (unit/2, unit -4),
    },
    "Nucleide_Sect": {
        "sizes": {
            "width": unit,
            "height": unit*3/4
        },
        "stroke_width": 0,
        "border_width": 0.2,
        "show_half_life": True,
        "half_life_font": 4,
        "half_life_offset": (1/2, 4),
        "show_energy": True,
        "energy_font": 4,
        "energy_offset": (0, unit),

    },
    "Legend": {
        "sizes": {
            "width": 8*unit,
            "height": 12*unit
        },
        "offset": (2*unit, 2*unit),
        "stroke_width": 0,
        "border_width": 1,
        "border_color": "black",
        "panel_background": "none",
        "show_title": True,
        "title_font": 18,
        "title_font_color": "black",
        "title_offset": (8*unit/2, unit),
        "show_decays_examples": True,
        "show_decays_examples_text": True,
        "decays_examples_font": 10,
        "decays_examples_offset": (unit/2, unit+unit/2),
        "decays_examples_font_offset": (unit/2+unit, unit/2+2.5),
        "decays_examples_font_color": "black",
        "show_nucleides_examples": True,
        "show_nucleides_examples_text": True,
        "nucleides_examples_font": 10,
        "nucleides_examples_offset": (unit/2, unit+10*unit+unit/2),
        "nucleides_examples_font_offset": (unit/2+unit, 10*unit+unit/2+2.5),
        "nucleides_examples_font_color": "black",
    },


    "colors": {
        "Stroke": "black",
        "Element_Box": "#FFFFFF",
        "Nucleide_Sect": "#FFFFFF",
        "DecayModes": {
            "ALPHA": {
                "fill": "#B3A60A",
                "text": "black"
            },
            "BETA_MINUS": {
                "fill": "#548088",
                "text": "black"
            },
            "STABLE": {
                "fill": "black",
                "text": "white"
            },
            "PROTON": {
                "fill": "#AD8516",
                "text": "black"
            },
            "SF": {
                "fill": "#295F2D",
                "text": "black"
            },
            "BETA_PLUS": {
                "fill": "#AF5E5B",
                "text": "black"
            },
            "IT": {
                "fill": "#C1BAB4",
                "text": "black"
            },
            "ELECTRON_CAPTURE": {
                "fill": "#646293",
                "text": "black"
            },
            "NEUTRON": {
                "fill": "#869898",
                "text": "black"
            }
        }
    },
}
# json_config = {}
# with open('/home/alfonso/Documents/TFG/testing/testing/data/3div_regular.json') as json_file:
#     json_config = json.load(json_file)

default_config = A_regular_detail_nodiv_config
