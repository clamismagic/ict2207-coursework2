# imports here
from .controller import Controller
import helper
import logging
import re
from typing import List

class Obfuscation:
    def __init__(self):
        pass
        # list to note which obfuscator has been used
        self.used_obfuscators: List[str] = []

    # obfuscation methods below!!
    def NOP_obfuscate(self):
        self.logger.info('Running "{0}" obfuscator'.format(self.__class__.__name__))

        try:
            op_codes = helper.get_nop_valid_op_codes()
            pattern = re.compile(r"\s+(?P<op_code>\S+)")

            for smali_file in helper.show_list_progress(
                self.get_smali_files(),
                interactive=self.interactive,
                description='Inserting "nop" instructions in smali files',
            ):
                self.logger.debug(
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
            self.logger.error(
                'Error during execution of "{0}" obfuscator: {1}'.format(
                    self.__class__.__name__, e
                )
            )
            raise

        finally:
            self.used_obfuscators.append(self.__class__.__name__)


