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

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 read_xml.py <path_to_xml_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    read_and_print_xml(file_path)