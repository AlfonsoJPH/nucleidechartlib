import argparse
import csv
import json
import xml.etree.ElementTree as ET
from element import Element
from element_table import ElementTable

def parse_args():
    parser = argparse.ArgumentParser(description="Generate nucleid charts from a CSV file.")
    parser.add_argument('--input-db', type=str, required=True, help="Input CSV file with nucleid data.")
    parser.add_argument('--output-file', type=str, required=True, help="Output SVG file.")
    parser.add_argument('--use-css', type=str, help="CSS file to style the SVG.")
    parser.add_argument('--use-json', type=str, help="JSON file with configuration for colors and sizes.")
    parser.add_argument('--use-xml', type=str, help="XML file with configuration for colors and sizes.")
    parser.add_argument('--with-colors', action='store_true', help="Include colors in the SVG.")
    parser.add_argument('--no-colors', action='store_true', help="Exclude colors from the SVG.")
    parser.add_argument('--show-decay-time', action='store_true', help="Show decay time in the SVG.")
    parser.add_argument('--num-cols', type=int, default=0, help="Number of columns in the chart.")
    parser.add_argument('--num-rows', type=int, default=0, help="Number of rows in the chart.")
    parser.add_argument('--divide-vertical', type=int, default=1, help="Vertical division factor.")
    parser.add_argument('--divide-horizontal', type=int, default=1, help="Horizontal division factor.")
    return parser.parse_args()

def load_elements_from_csv(filename):
    elements = []
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            element = Element(
                symbol=row['Element'],
                atomic_number=int(row['AtomicNumber']),
                atomic_weight=int(row['MassNumber']),
                # Add other necessary fields here
            )
            # Add decay modes and other attributes here
            elements.append(element)
    return elements

def load_config(filename, filetype='json'):
    if filetype == 'json':
        with open(filename, 'r') as f:
            return json.load(f)
    elif filetype == 'xml':
        tree = ET.parse(filename)
        root = tree.getroot()
        # Parse XML accordingly
        return root

def main():
    args = parse_args()

    elements = load_elements_from_csv(args.input_db)

    if args.use_json:
        config = load_config(args.use_json, 'json')
    elif args.use_xml:
        config = load_config(args.use_xml, 'xml')
    else:
        config = None

    table = ElementTable(elements, div=args.divide_vertical, rows=args.num_rows, cols=args.num_cols, config=config)

    if args.with_colors and not args.no_colors:
        table.apply_colors()

    table.draw(args.output_file)

    if args.use_css:
        table.set_style(args.output_file, args.use_css)

if __name__ == "__main__":
    main()
