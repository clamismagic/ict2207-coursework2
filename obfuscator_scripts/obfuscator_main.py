# imports here
# from obfuscator_scripts import helper # pycharm
import helper # vscode
import re
import random
from typing import List
import xml.etree.cElementTree as Xml
from xml.etree.cElementTree import Element


class Obfuscator:
    def __init__(self):
        # TODO: implement checklist for obfuscator selection
        self.op_codes = helper.get_nop_op_codes()
        self.pattern = re.compile(r"\s+(?P<op_code>\S+)") #can try r'^([ ]*)(?P<opCode>([^ ]+)
        self.locals_pattern = re.compile(r"\s+\.locals\s(?P<local_count>\d+)")

    def nop_obfuscator(self, smali_file: str):
        try:
            print(
                'Inserting "nop" instructions in file "{0}"'.format(smali_file)
            )
            with helper.inplace_edit_file(smali_file) as (in_file, out_file):
                for line in in_file:

                    # Print original instruction.
                    out_file.write(line)

                    # Check if this line contains an op code at the beginning
                    # of the string.
                    match = self.pattern.match(line)
                    if match:
                        op_code = match.group("op_code")
                        # If this is a valid op code, insert some nop instructions
                        # after it.
                        if op_code in self.op_codes:
                            nop_count = helper.get_random_int(1, 5) #Randomize the number of nop(s)
                            out_file.write("\tnop\n" * nop_count)

        except Exception as e:
            print(
                'Error during execution of NOP obfuscator: {0}'.format(e)
            )
            raise

    def goto_obfuscator(self, smali_file: str):
        try:
            print(
                'Inserting "goto" instructions in file "{0}"'.format(smali_file)
            )
            with helper.inplace_edit_file(smali_file) as (read_file, write_file):
                editing_method = False
                for line in read_file:
                    if (
                            line.startswith(".method ")
                            and " abstract " not in line
                            and " native " not in line
                            and not editing_method
                    ):
                        # If at the beginning of a non abstract/native method
                        # (after the .locals instruction), insert a "goto" to the
                        # label at the end of the method and a label to the first
                        # instruction of the method.
                        write_file.write(line)
                        editing_method = True

                    elif editing_method and self.locals_pattern.match(line):
                        write_file.write(line)
                        write_file.write("\n\tgoto/32 :after_last_instruction\n\n")
                        write_file.write("\t:before_first_instruction\n")

                    elif line.startswith(".end method") and editing_method:
                        # If at the end of the method, insert a label after the
                        # last instruction of the method and a "goto" to the label
                        # at the beginning of the method. This will not cause an
                        # endless loop because the method will return at some point
                        # and the second "goto" won't be called again when the
                        # method finishes.
                        write_file.write("\n\t:after_last_instruction\n\n")
                        write_file.write("\tgoto/32 :before_first_instruction\n\n")
                        write_file.write(line)
                        editing_method = False

                    else:
                        write_file.write(line)
        except Exception as e:
            print(
                'Error during execution of goto obfuscator: {0}'.format(e)
            )
            raise

    def method_rename(self, smali_file: str):
        try:
            print(
                'Renaming methods in file "{0}"'.format(smali_file)
            )

        except Exception as e:
            print(
            'Error during execution of method renaming: {0}'.format(e)
            )
            raise

    def opaque_predicate(self, smali_file: str):
        try:
            print(
                'Inserting opaque predicate expressions in file "{0}"'.format(smali_file)
            )

        except Exception as e:
            print(
            'Error during execution of opaque predicate expressions: {0}'.format(e)
            )
            raise

# obfuscation methods below!!

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

