import csv
import re
from ..nucleids_chart.element import DecayMode, Element

def read_elements(file_name):
    with open(file_name, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        elements = set()
        for row in reader:
            element = Element(remove_numbers(row['A Element']), int(row['Atomic Number']), int(row['Mass Number']))
            set_decay_modes(row['Decay Modes and their Intensities'], element)
            elements.add(element)

    return elements

def set_decay_modes(modes, element):
    data = transform_data(modes)
    for mode in data.split(' '):
        value, key = extract_value(mode)
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
    datos = re.sub(r'[+-;]', '', datos)
    datos = re.sub(r'[><]', '=', datos)
    datos = re.sub(r'\?', '=1', datos)
    return datos

def extract_value(mode):
    number = re.findall(r'\d+', mode)
    value = int(number[0]) if number else 1
    key = re.sub(r'\d+', '', mode)
    return value, key

def remove_numbers(data):
    return re.sub(r'\d+', '', data)
