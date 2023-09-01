import os
import re
import xml.etree.ElementTree as ET

from draw import draw

def parse_XML(file_path: str) -> list:
    """Parses a given XML file and returns a list of bounds for each UI element of the file."""

    def traverse(root: ET.Element):
        """Traverse all levels of the XML tree to find all nested node elements."""

        if root is not None:
            if root.tag == "node":
                bounds = root.attrib.get("bounds")
                bounds = re.findall("\[(.*?)\]", bounds)
                bounds = [bound.split(",") for bound in bounds]
                bounds = [int(bound) for sublist in bounds for bound in sublist]

                bound_list.append(bounds)

            for child in root.findall("node"):
                traverse(child)

    bound_list = []

    tree = ET.parse(file_path)
    root = tree.getroot()
  
    # Traverse all children in the XML structure
    traverse(root)

    return bound_list


if __name__ == "__main__":
    data_files = []
    data_directory = "Programming-Assignment-Data"

    files = os.listdir(data_directory)

    for file in files:
        if ".xml" in file:
            data_files.append(file)

    bound_list = parse_XML(os.path.join(data_directory, data_files[0]))
    draw(os.path.join(data_directory, data_files[0].replace(".xml", ".png")), bound_list)