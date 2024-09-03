import csv
import json
import xml.etree.ElementTree as ET
from nucleidechartlib.element.element import Element
from nucleidechartlib.element.nucleide import Nucleide
from nucleidechartlib.enums import DecayMode


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
