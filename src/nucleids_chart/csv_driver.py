import csv
import re
from ..nucleids_chart.element import DecayMode, Element

def read_elements(file_name):
    with open(file_name, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        elements = set()
        for row in reader:
            element = Element(remove_numbers(row['A Element']), int(int(row['Atomic Number'])/10), int(row['Mass Number']))
            set_decay_modes(row['Decay Modes and their Intensities'], element)
            elements.add(element)

    return elements

def set_decay_modes(modes, element):
    data = transform_data(modes)
    #escribir en archivo debug.txt la linea data
    for mode in data.split(' '):
        open("debug_mode.txt", "a").write(mode + "\n")
        value, key = extract_value(mode)
        open("debug_key.txt", "a").write(key + "\n")

        switch_case = {
            'A': DecayMode.ALPHA,
            'B+': DecayMode.BETA_PLUS,
            'B-': DecayMode.BETA_MINUS,
            'EC': DecayMode.ELECTRON_CAPTURE,
            'IS': DecayMode.ISOMER,
            'p': DecayMode.PROTON,
            'n': DecayMode.NEUTRON,
            'SF': DecayMode.SF
        }
        if key in switch_case:
            element.decay_modes_and_intensities.append((switch_case[key], value))


def transform_data(datos):
    datos = re.sub(r'~', '=', datos)
    datos = re.sub(r';', ' ', datos)
    datos = re.sub(r'(?<!B)[+-]', '', datos)
    datos = re.sub(r'[><]', '=', datos)
    datos = re.sub(r'\?', '=1', datos)
    datos = re.sub(r'\s*=\s*', '=', datos)
    return datos


def extract_value(mode):
    # Ajustamos la expresión regular para capturar números enteros y decimales correctamente
    number = re.findall(r'\d*\.?\d+', mode)
    value = 1.0
    # Verificamos si 'number' contiene algún elemento y si ese elemento no es una cadena vacía
    if number and number[0]:
        value = float(number[0])
    key = re.sub(r'\d*\.?\d+', '', mode)
    key = re.sub(r'=', '', key)
    return value, key

def remove_numbers(data):
    return re.sub(r'\d+', '', data)
