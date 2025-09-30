#!/usr/bin/python3
"""Module serializes and deserializes with XML."""


import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Method takes Python dictionary and filename parameters and
    serializes dictionary into XML."""


    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)  # converts value to string for XML text

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)

def deserialization_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()

    result = {}
    for child in root:
        key = child.tag
        value = child.text

        if value == "True":
            value = True
        elif value == "False":
            value = False
        else:
            try:
                if '.' in value:
                    value = float(value)
                else:
                    value = int(value)
            except (ValueError, TypeError):
                pass

        result[key] = value

    return result
