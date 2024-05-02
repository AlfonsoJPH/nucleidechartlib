import svgwrite
from .element_box import ElementBox

tamanos_estandar_A = {
    "A0": ("841mm", "1189mm"),
    "A1": ("594mm", "841mm"),
    "A2": ("420mm", "594mm"),
    "A3": ("297mm", "420mm"),
    "A4": ("297mm", "210mm"),
    "A5": ("148mm", "210mm"),
    "A6": ("105mm", "148mm"),
    "A7": ("74mm", "105mm"),
    "A8": ("52mm", "74mm"),
    "A9": ("37mm", "52mm"),
    "A10":("26mm", "37mm")
}

class ElementTable:
    def __init__(self, elements, format='A4', div=1):
        self.elements = elements
        self.table = set()
        self.format = format
        self.div = div
        self.rows = 0
        self.columns = 0

        for element in elements:
            self.add_element(element)


    def draw(self, filename, style='None'):
        dwg = svgwrite.Drawing(filename, profile='tiny', size=tamanos_estandar_A[self.format], viewBox=('0 0 297 210'))
        self.draw_border(dwg)
        for box in self.table:
            box.draw(dwg)
        # self.draw_legend(dwg)
        dwg.save()
        if style != 'None':
            self.set_style(filename, style)


    def draw_border(self, dwg):
        rect = dwg.rect(insert=(10, 10), size=(287, 200), fill="white" )
        dwg.add(rect)

    def draw_legend(self, dwg):
        legend = dwg.g(id="legend" )

        panel = legend.rect(insert=(287, 20), size="40 60")
        title = legend.text(_class="title", text="Leyenda")

        alpha_rect = legend.rect(rx=5,ry=5, size="2 2", _class="Alpha")
        alpha_text = legend.text(rx=10, ry=5, text="Alpha")


        dwg.add(legend)


    def set_style(self, filename, style):
        with open(filename, "r") as original:
            original = original.read()

        style_line = "<?xml-stylesheet type=\"text/css\" href=\"" + style + "\" ?>\n"

        with open(filename, "w") as modified:
            modified.write(style_line + original)





    def add_element(self, element):
        box = ElementBox(element, self.div, self.rows, self.columns)
        self.table.add(box)
        self.rows = max(self.rows, box.y)
        self.columns = max(self.columns, box.x)
