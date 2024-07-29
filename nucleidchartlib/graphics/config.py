# .ALPHA {
#   rect:not(.border) {
#     fill: #B3A60A;
#   }
#   fill: #B3A60A;
# }


# .BETA_MINUS {
#     rect:not(.border) {
#       fill: #548088;
#   }
#   fill: #548088;
# }


# .ELECTRON_CAPTURE {
#   rect:not(.border) {
#     fill: #76C848;
#   }
#   fill: #76C848;
# }

# .STABLE {
#   rect:not(.border) {
#     fill: black;
#   }
#   fill: black;

#   text{
#     fill:white;
#   }
# }

# .PROTON {
#   rect:not(.border) {
#     fill: #AD8516;
#   }
#   fill: #AD8516;
# }

# .NEUTRON {
#   rect:not(.border) {
#     fill: #DC5FCD;
#   }
#   fill: #DC5FCD;
# }

# .SF {
#   rect:not(.border){
#     fill: #295F2D;
#   }
#   fill: #295F2D;
# }

# .BETA_PLUS {
#   rect:not(.border) {
#     fill: #AF5E5B;
#   }
#   fill: #AF5E5B;
# }

# .IT {
#   rect:not(.border) {
#     fill: #C1BAB4;
#   }
#   fill: #C1BAB4;
# }

# .ELECTRON_CAPTURE {
#   rect:not(.border) {
#     fill: #646293;
#   }
#   fill: #646293;
# }

# .NEUTRON {
#   rect:not(.border) {
#     fill: #869898;
#   }
#   fill: #869898;
# }

#Dictionary with the configs for the table, boxes and sections
#parameters of the box
#        color = config.get("colors", {}).get("Box", "#FFFFFF")
        # stroke_color = config.get("colors", {}).get("Stroke", "black")
        # stroke_width = config.get("sizes", {}).get("stroke_width", 0)
        # border_width = config.get("sizes", {}).get("border_width", 1)
        # text_color = config.get("colors", {}).get("Text", "black")
        # font_size = config.get("sizes", {}).get("font1", 4)
        # size = config.get("cell_sizes", {"width": 40, "height": 40})

default_config = {
    "Table": {
        "color": "#FFFFFF",
        "Text": "black",
        "font1": "30px",
        "font2": "20px",
        "font3": "10px",
        "sizes": { "width": 21000, "height": 29700 }
    },
    "Element_Box": {
        "sizes": {
            "width": 40,
            "height": 40
        },
        "stroke_width": 0,
        "border_width": 1,
        "font1": 7
    },
    "Nucleide_Sect": {
        "sizes": {
            "width": 40,
            "height": 30
        },
        "stroke_width": 1,
        "border_width": 1,
        "font1": 4
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
            "ELECTRON_CAPTURE": {
                "fill": "#76C848",
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
    "Divisions": {
        "default": "4",
        3: { (1, 32), (33, 64), (65, 96) },
        4: { (1, 24), (25, 48), (49, 72), (73, 96) },
        5: { (1, 20), (21, 40), (41, 60), (61, 80), (81, 100) }
    }


}
