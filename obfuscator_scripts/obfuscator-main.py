# imports here
import helper
import re
from typing import List


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

