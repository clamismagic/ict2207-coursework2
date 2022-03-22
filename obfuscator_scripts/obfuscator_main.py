# imports here
# from obfuscator_scripts import helper # pycharm
import helper # vscode
import re
import random
from typing import List


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


    #Random Android Manifest line sequence
    def rand_manifest(self, AndroidManifest: str):
        try:
            print(
                'Inserting "randomManifest" instructions in file "{0}"'.format(AndroidManifest)
            )
            
            Uses = []               #This list is to store line that start with "<uses"
            Application = []        #This list is to store lines that met certain critiria and is also a child in the <Application> parent
            appLineNum = []         #Works together with Application list by storing the line number
            app_start = 0           #Initilise app_start
            app_stop = 0            #Initilise app_stop
            lineNumberList = []     #Works together with Uses list by storing the line number
            lineNumber = 0          #Initilise lineNumber

            #Get file path and open file to read and write
            with helper.inplace_edit_file(AndroidManifest) as (in_file, out_file):

                #1st loop to find line that begins with "uses-"
                for line in in_file:
                    
                    #replace all android: to obfuscation:
                    newLine = line.replace('android:', 'obfuscation:')
                    line = newLine

                    #Add line that start with     <uses-" and their line number to their respective list
                    if (line.startswith("    <uses-")):
                        Uses.append(line)
                        lineNumberList.append(lineNumber)

                    #To get app_start for the next loop
                    if (line.startswith("    <application")):
                        app_start = lineNumber
                    
                    #To get app_stop for the next loop
                    if (line.startswith("    </application>")):
                        app_stop = lineNumber

                    lineNumber += 1

                #Going back to start of file
                in_file.seek(0)
                lineNumber = 0

                #Loop 2 to find line that start with "        <" but not "        <activity" or "        <service" or "        </"
                for line in in_file:

                    #replace all android: to obfuscation:
                    newLine = line.replace('android:', 'obfuscation:')
                    line = newLine

                    #If lineNumber is between <application> parent
                    if ((lineNumber > app_start) and (lineNumber < app_stop)):
                        if (
                            (line.startswith("        <"))
                            and not (line.startswith("        <activity"))
                            and not (line.startswith("        <service"))
                            and not (line.startswith("        </"))
                        ):
                            Application.append(line)
                            appLineNum.append(lineNumber)
                    
                    lineNumber += 1


                #Shuffle Uses list
                random.shuffle(Uses)

                #Shuffle Application list
                random.shuffle(Application)

                #Going back to start of file
                in_file.seek(0)
                lineNumber = 0

                #Begins printing in out_file
                for line in in_file:

                    #Remove the xml information in line 0
                    if (lineNumber == 0):
                        line = re.sub('^.*<', '<', line)

                    #replace all "android:" to "obfuscation:"
                    newLine = line.replace('android:', 'obfuscation:')
                    line = newLine

                    #This loop manage the line that is after the line that begines with <uses-
                    #If lineNumberList list is not empty
                    if lineNumberList:

                        #If the current line nymber is not in the list, do not modify line
                        if lineNumber != lineNumberList[0]:
                            out_file.write(line)
                        
                        else:
                            lineNumberList.pop(0)
                            # Add the first element in the shuffled list of line that begin with "    <uses-"
                            out_file.write(Uses[0])

                            #If Uses list not empty, remove the first element
                            if Uses:
                                Uses.pop(0)
                    
                    else:

                        #This loop manage the line that is after the line <application
                        #If appLineNum list not empty
                        if appLineNum: 

                            #If the current line nymber is not in the list, do not modify line
                            if lineNumber != appLineNum[0]:
                                out_file.write(line)

                            #If line is in the list, replace it with the first element in Application list then remove the first element in appLineNum list
                            else:
                                appLineNum.pop(0)
                                out_file.write(Application[0])

                                #If Application list not empty, remove the first element
                                if Application:
                                    Application.pop(0)

                        else:
                            # if both Appliaiton list and Uses list are empty, print the remaining lines
                            out_file.write(line)
                        
                    lineNumber += 1

        except Exception as e:
            print(
                'Error during execution of randomManifest obfuscator: {0}'.format(e)
            )
            raise