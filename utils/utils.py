import csv
import json
import xml.etree.ElementTree as ET
from element import Element, DecayMode

def load_elements_from_csv(file_path):
    elements = []
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            element = Element(
                symbol=row['Element'],
                atomic_number=int(row['Atomic Number']),
                atomic_weight=int(row['Mass Number'])
            )
            # Set additional properties
            element.isomer = bool(row['Isomer'])
            element.mass_excess = float(row['Mass Excess'])
            element.mass_excess_uncertainty = float(row['Mass Excess uncertainty'])
            element.isomer_excitation_energy = float(row['Isomer Excitation Energy'])
            element.isomer_excitation_energy_uncertainty = float(row['Isomer Excitation Energy uncertainty'])
            element.ensdf_year = int(row['Ensdf year'])
            element.year_of_discovery = int(row['Year of Discovery'])

            # Parse decay modes and intensities
            if 'Decay Modes and their Intensities' in row:
                decay_modes = row['Decay Modes and their Intensities'].split(';')
                for decay_mode in decay_modes:
                    mode, intensity = decay_mode.split(':')
                    element.add_decay_mode_and_intensity(DecayMode[mode.strip()], float(intensity.strip()))

            elements.append(element)
    return elements

def load_config_from_json(file_path):
    with open(file_path, 'r') as json_file:
        config = json.load(json_file)
    return config

def load_config_from_xml(file_path):
    config = {}
    tree = ET.parse(file_path)
    root = tree.getroot()
    for child in root:
        config[child.tag] = child.text
    return config

def read_config(file_path):
    """
    Lee un archivo de configuración en formato JSON y devuelve su contenido como un diccionario.

    :param file_path: Ruta al archivo JSON de configuración
    :return: Diccionario con la configuración
    """
    with open(file_path, 'r') as file:
        config = json.load(file)
    return config

def update_config(default_config, provided_config):
    config = default_config.copy()

    for key, value in provided_config.items():
        if key in config:
            if isinstance(config[key], dict) and isinstance(value, dict):
                config[key].update(value)
            else:
                config[key] = value

    return config
