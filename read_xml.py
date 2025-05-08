"""
This script provides functionality to read and print the structure of an XML file.

Functions:
- read_and_print_xml(file_path): Parses the XML file at the given path and prints its structure.

Usage:
Run the script and provide the path to an XML file when prompted.
"""

import xml.etree.ElementTree as ET

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
    file_path = input("Enter the path to the XML file: ")
    read_and_print_xml(file_path)