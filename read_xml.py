"""
This script provides functionality to read and print the structure of an XML file.

Functions:
- read_and_print_xml(file_path): Parses the XML file at the given path and prints its structure.

Usage:
Run the script and provide the path to an XML file as a command-line argument.
"""

import xml.etree.ElementTree as ET
import sys

def read_and_print_xml(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()

        for child in root:
            print(f"Tag: {child.tag}, Attributes: {child.attrib}")
            for subchild in child:
                print(f"  Subtag: {subchild.tag}, Text: {subchild.text}, Attributes: {subchild.attrib}")
    except Exception as e:
        print(f"Error reading XML file: {e}")

def validate_xml(root):
    for item in root.findall('item'):
        details = item.find('details')
        if details is not None:
            price = float(details.find('price').text)
            stock = int(details.find('stock').text)
            if price < 0 or stock < 0:
                raise ValueError(f"Invalid data in item '{item.attrib.get('name', 'unknown')}': price={price}, stock={stock}")

def validate_xml_structure(root):
    if root is None or not list(root):
        raise ValueError("Invalid XML structure: Root element is empty or missing child elements.")

# Update the main function to include general structure validation
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 read_xml.py <path_to_xml_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        validate_xml_structure(root)
        read_and_print_xml(file_path)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)