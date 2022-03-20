# imports here
import helper
import re
import random
from typing import List
import xml.etree.cElementTree as Xml
from xml.etree.cElementTree import Element


class Obfuscation:
    def __init__(self):
        pass

    # obfuscation methods below!!
    def nop_obfuscate(self, smali_files: List[str]):
        print('Running NOP obfuscator')

        try:
            op_codes = helper.get_nop_valid_op_codes()
            pattern = re.compile(r"\s+(?P<op_code>\S+)")

            for smali_file in smali_files:
                print(
                    'Inserting "nop" instructions in file "{0}"'.format(smali_file)
                )
                with helper.inplace_edit_file(smali_file) as (in_file, out_file):
                    for line in in_file:

                        # Print original instruction.
                        out_file.write(line)

                        # Check if this line contains an op code at the beginning
                        # of the string.
                        match = pattern.match(line)
                        if match:
                            op_code = match.group("op_code")
                            # If this is a valid op code, insert some nop instructions
                            # after it.
                            if op_code in op_codes:
                                nop_count = helper.get_random_int(1, 5)
                                out_file.write("\tnop\n" * nop_count)

        except Exception as e:
            print(
                'Error during execution of NOP obfuscator: {0}'.format(e)
            )
            raise

#    def indent_xml(self, element: Element, level=0):
#        indentation = "\n" + level * "    "
#        if len(element):
#            if not element.text or not element.text.strip():
#                element.text = indentation + "    "
#            if not element.tail or not element.tail.strip():
#                element.tail = indentation
#            for element in element:
#                self.indent_xml(element, level + 1)
#            if not element.tail or not element.tail.strip():
#                element.tail = indentation
#        else:
#            if level and (not element.tail or not element.tail.strip()):
#                element.tail = indentation
#
#    def xml_elements_equal(self, one: Element, other: Element) -> bool:
#        if type(one) != type(other):
#            return False
#        if one.tag != other.tag:
#            return False
#
#        if one.text and other.text:
#            if one.text.strip() != other.text.strip():
#                return False
#        elif one.text != other.text:
#            return False
#
#        if one.tail and other.tail:
#            if one.tail.strip() != other.tail.strip():
#                return False
#        elif one.tail != other.tail:
#            return False
#
#        if one.attrib != other.attrib:
#            return False
#        if len(one) != len(other):
#            return False
#
#        return all(self.xml_elements_equal(e1, e2) for e1, e2 in zip(one, other))
#
#    def remove_xml_duplicates(self, root: Element):
#
#        # Recursively eliminate duplicates starting from children nodes.
#        for element in root:
#            self.remove_xml_duplicates(element)
#
#        non_duplicates = []
#        elements_to_remove = []
#
#        # Find duplicate nodes which have the same parent node.
#        for element in root:
#            if any(self.xml_elements_equal(element, nd) for nd in non_duplicates):
#                elements_to_remove.append(element)
#            else:
#                non_duplicates.append(element)
#
#        # Remove existing duplicates at this level.
#        for element_to_remove in elements_to_remove:
#            root.remove(element_to_remove)
#
#    def scramble_xml_element(self, element: Element):
#        children = []
#
#        # Get the children of the current element.
#        for child in element:
#            children.append(child)
#
#        # Remove the children from the current element (they will be added later
#        # in a different order).
#        for child in children:
#            element.remove(child)
#
#        # Shuffle the order of the children of the element and add them again to
#        # the element. Then repeat the scramble operation recursively.
#        random.shuffle(children)
#        for child in children:
#            element.append(child)
#            self.scramble_xml_element(child)
#
#    def obfuscate(self, xml_file):
#
#        try:
#            '''
#            # Change default namespace.
#            Xml.register_namespace(
#                "obfuscation", "http://schemas.android.com/apk/res/android"
#            )
#
#            xml_parser = Xml.XMLParser(encoding="utf-8")
#            manifest_tree = Xml.parse(
#                obfuscation_info.get_manifest_file(), parser=xml_parser
#            )
#            '''
#
#            manifest_root = xml_file
#            self.remove_xml_duplicates(manifest_root)
#            self.scramble_xml_element(manifest_root)
#            self.indent_xml(manifest_root)
#
#            '''
#            # Write the changes into the manifest file.
#            manifest_tree.write(obfuscation_info.get_manifest_file(), encoding="utf-8")
#            '''
#
#        except Exception as e:
#            print ('Error during execution of randManifest_obfuscate: {0}'.format(e))
#            raise

