import xml.etree.ElementTree as ET
from xml.dom import minidom
import json

def json_to_xml(json_obj):
    elem = ET.Element("root")

    def build_tree(d, parent):
        if isinstance(d, dict):
            for key, value in d.items():
                sub_elem = ET.SubElement(parent, key)
                build_tree(value, sub_elem)
        elif isinstance(d, list):
            for item in d:
                item_elem = ET.SubElement(parent, "item")
                build_tree(item, item_elem)
        else:
            parent.text = str(d)

    build_tree(json_obj, elem)
    return elem

def prettify_xml(elem):
    """Retorna uma string XML formatada e bonita."""
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")