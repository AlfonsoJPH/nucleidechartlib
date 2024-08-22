import csv
import re
from nucleidechartlib.element.element import Element
from nucleidechartlib.element.nucleide import Nucleide
from nucleidechartlib.enums import DecayMode

def read_elements(file_name):
    with open(file_name, newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        temp_sym = ""
        temp_Elem = Element(id=-1, symbol="dummy", atomic_number=-1, mass_number=-1, nucleides={})
        id_elem = 0
        id_nucleide = 0

        elements = dict()
        for row in reader:
            if row['Decay Modes and their Intensities'] == '':
                continue
            symbol = row['A Element']
            if temp_sym != symbol:
                if temp_Elem and temp_Elem.id != -1:
                    elements[id_elem]=temp_Elem
                temp_sym = symbol
                temp_Elem = Element(id=id_elem, symbol=remove_numbers(symbol),
                                    atomic_number=int(int(row['Atomic Number']) / 10),
                                    mass_number=int(row['Mass Number']),
                                    nucleides={})
                id_elem += 1

            half_life = row['Half-life']
            if row['Half-life unit'] != '':
                half_life += " " + row['Half-life unit']
            year_of_discovery = row['Year of Discovery']

            if year_of_discovery is not int():
                year_of_discovery = 0

            mass_excess = row['Mass Excess']
            if mass_excess is not float():
                mass_excess = 0.0

            nucleide = Nucleide(id=id_nucleide,
                                mass_excess=float(mass_excess),
                                half_life=half_life,
                                decay_modes_intensities={},
                                energy_levels={},
                                spin_and_parity=row['Spin and Parity'],
                                year_of_discovery=int(year_of_discovery))
            id_nucleide += 1


            set_decay_modes(row['Decay Modes and their Intensities'], nucleide)
            stable = nucleide.decay_modes_intensities.get(DecayMode.STABLE)
            if stable != None:
                nucleide.half_life = str(stable)
            temp_Elem.nucleides[nucleide.id] = nucleide


    elements[id_elem]=temp_Elem
    return elements

def read_element(file_name, n):
    with open(file_name, newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        temp_Elem = Element(id=-1, symbol="dummy", atomic_number=-1, mass_number=-1, nucleides={})
        id_elem = 0
        id_nucleide = 0

        found=False
        temp_Elem = Element(id=-1, symbol="",
                                atomic_number=-1,
                                mass_number=-1,
                                nucleides={})
        # get row n of reader
        for row in reader:
            if(found and row['A Element'] != n):
                return temp_Elem

            if row['A Element'] != n  or row['Decay Modes and their Intensities'] == '':
                continue
            symbol = row['A Element']
            if(not found):
                temp_Elem = Element(id=id_elem, symbol=remove_numbers(symbol),
                                    atomic_number=int(int(row['Atomic Number']) / 10),
                                    mass_number=int(row['Mass Number']),
                                    nucleides={})

            half_life = row['Half-life']
            if row['Half-life unit'] != '':
                half_life += " " + row['Half-life unit']
            year_of_discovery = row['Year of Discovery']

            if year_of_discovery is not int():
                year_of_discovery = 0

            mass_excess = row['Mass Excess']
            if mass_excess is not float():
                mass_excess = 0.0

            nucleide = Nucleide(id=id_nucleide,
                                mass_excess=float(mass_excess),
                                half_life=half_life,
                                decay_modes_intensities={},
                                energy_levels={},
                                spin_and_parity=row['Spin and Parity'],
                                year_of_discovery=int(year_of_discovery))
            id_nucleide += 1


            set_decay_modes(row['Decay Modes and their Intensities'], nucleide)
            stable = nucleide.decay_modes_intensities.get(DecayMode.STABLE)
            if stable != None:
                nucleide.half_life = str(stable)
            temp_Elem.nucleides[nucleide.id] = nucleide


        return temp_Elem



def set_decay_modes(modes, nucleide):
    data = transform_data(modes)
    for mode in data.split(' '):
        value, key = extract_value(mode)

        switch_case = {
            'A': DecayMode.ALPHA,
            'B+': DecayMode.BETA_PLUS,
            'B-': DecayMode.BETA_MINUS,
            'EC': DecayMode.ELECTRON_CAPTURE,
            'IS': DecayMode.STABLE,
            'IT': DecayMode.IT,
            'p': DecayMode.PROTON,
            'n': DecayMode.NEUTRON,
            'SF': DecayMode.SF
        }
        if key in switch_case:
            nucleide.decay_modes_intensities[switch_case[key]] = value

def transform_data(datos):
    datos = re.sub(r'~', '=', datos)
    datos = re.sub(r';', ' ', datos)
    datos = re.sub(r'\[', ' ', datos)
    datos = re.sub(r'(?<!B)[+-]', '', datos)
    datos = re.sub(r'[><]', '=', datos)
    datos = re.sub(r'\?', '=1', datos)
    datos = re.sub(r'\s*=\s*', '=', datos)
    return datos

def extract_value(mode):
    number = re.findall(r'\d*\.?\d+', mode)
    value = 1.0
    if number and number[0]:
        value = float(number[0])
    key = re.sub(r'\d*\.?\d+', '', mode)
    key = re.sub(r'=', '', key)
    return value, key

def remove_numbers(data):
    return re.sub(r'\d+', '', data)
