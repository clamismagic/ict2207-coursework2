# imports here
import os
import subprocess
from typing import List, Union


class Controller:
    """
    This class contains all the functions that are required to bridge the application UI
    to the backend operations, decompilation, obfuscation, recompilation and signing of
    application to APK format.
    During the execution of the application, one instance of this class should be instantiated
    in order to invoke the backend functions.
    """

    def __init__(self,
                 apk_path: str,
                 keystore_file: str = None,
                 keystore_passwd: str = None,
                 key_alias: str = None,
                 key_passwd: str = None
                 ):
        """
        handle inputs by user for file locations

        :param apk_path: string that represents the full path to the APK to be obfuscated
        :param keystore_file: string that represents the full path to the keystore file used to sign the application
        :param keystore_passwd: string that represents the password mapped to the user's specified keystore file
        :param key_alias: string that represents the key alias used for the specified keystore file
        :param key_passwd: string that represents the password mapped to the specified key alias
        """
        self.apk_path: str = apk_path
        self.working_dir_path: str = os.path.join(os.path.dirname(self.apk_path),
                                                  os.path.splitext(os.path.basename(self.apk_path))[0],
                                                  "decompiled_files")
        self.output_apk_path: str = os.path.join(os.path.dirname(self.apk_path),
                                                 os.path.splitext(os.path.basename(self.apk_path))[0],
                                                 "output_files/",
                                                 os.path.splitext(os.path.basename(self.apk_path))[0],
                                                 "_obfuscated.apk")
        self.keystore_file: str = keystore_file
        self.keystore_passwd: str = keystore_passwd
        self.key_alias: str = key_alias
        self.key_passwd: str = key_passwd
        self.manifest_file: Union[str, None] = None
        self.smali_files: List[str] = []
        self.native_lib_files: List[str] = []

        # check if specified APK is valid
        if not os.path.isfile(self.apk_path):
            print('Unable to find file "{0}"'.format(self.apk_path))
            raise FileNotFoundError('Unable to find file "{0}"'.format(self.apk_path))

        if not os.path.isdir(self.working_dir_path):
            try:
                os.makedirs(self.working_dir_path, exist_ok=True)
            except Exception as e:
                print(
                    'Unable to create working directory "{0}": {1}'.format(
                        self.working_dir_path, e
                    )
                )
                raise

        # decompile apk into smali
        self.decompile_apk()

        return

    def decompile_apk(self):
        # The input apk will be decoded with apktool
        apktools_path = "../tools/apktool.jar"
        cmd = "java -jar {0} d \"{1}\" -o \"{2}\" --force".format(apktools_path, self.apk_path, self.working_dir_path)

        try:
            print('Running decode command "{0}"'.format(cmd))

            # A new line character is sent as input since newer versions of Apktool
            # have an interactive prompt on Windows where the user should press a key.
            output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, input=b"\n").strip()

            if b"Exception in thread " in output:
                # Report exception raised in Apktool.
                raise subprocess.CalledProcessError(1, cmd, output)

            # Path to the decoded manifest file.
            self.manifest_file = os.path.join(
                self.working_dir_path, "AndroidManifest.xml"
            )

            # generate a list containing the paths to all the relevant smali files obtained with apktool
            self.smali_files = [
                os.path.join(root, file_name)
                for root, dir_names, file_names in os.walk(self.working_dir_path)
                for file_name in file_names
                if file_name.endswith(".smali")
            ]

            # remove known libraries to only grab smali files directly representing the main app
            with open("../tools/libs_to_ignore.txt", "r", encoding="utf-8") as file:
                read_libs_to_ignore = list(filter(None, (line.rstrip() for line in file)))

                # Normalize paths for the current OS ('.join(x, "")' is used to add a trailing slash).
            libs_to_ignore = list(
                map(
                    lambda x: os.path.join(os.path.normpath(x), ""),
                    read_libs_to_ignore,
                )
            )

            filtered_smali_files = []

            for smali_file in self.smali_files:
                # Get the path without the initial part <root>/smali/.
                relative_smali_file = os.path.join(
                    *(
                        os.path.relpath(
                            smali_file, self.working_dir_path
                        ).split(os.path.sep)[1:]
                    )
                )
                # Get only the smali files that are not part of known third
                # party libraries.
                if not any(
                        relative_smali_file.startswith(lib)
                        for lib in libs_to_ignore
                ):
                    filtered_smali_files.append(smali_file)

            self.smali_files = filtered_smali_files

            # Sort the list of smali files to always have the list in the same order.
            self.smali_files.sort()

            # A list containing the paths to the native libraries included in the application.
            self.native_lib_files = [
                os.path.join(root, file_name)
                for root, dir_names, file_names in os.walk(
                    os.path.join(self.working_dir_path, "lib")
                )
                for file_name in file_names
                if file_name.endswith(".so")
            ]

            # Sort the list of native libraries to always have the list in the same order.
            self.native_lib_files.sort()
            return
        except subprocess.CalledProcessError as e:
            print(
                "Error during decode command: {0}".format(
                    e.output.decode(errors="replace") if e.output else e
                )
            )
            raise
        except Exception as e:
            print("Error: {0}".format(e))
            raise
