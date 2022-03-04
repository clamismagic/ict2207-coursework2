# imports here
import os


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
                 working_dir_path: str = None,
                 output_apk_path: str = None,
                 keystore_file: str = None,
                 keystore_passwd: str = None,
                 key_alias: str = None,
                 key_passwd: str = None
                 ):
        """
        handle inputs by user for file locations

        :param apk_path: string that represents the full path to the APK to be obfuscated
        :param working_dir_path: string that represents the custom working directory to write obfuscated files
        :param output_apk_path: string that represents the full path to output the recompiled APK after obfuscation
        :param keystore_file: string that represents the full path to the keystore file used to sign the application
        :param keystore_passwd: string that represents the password mapped to the user's specified keystore file
        :param key_alias: string that represents the key alias used for the specified keystore file
        :param key_passwd: string that represents the password mapped to the specified key alias
        """
        self.apk_path: str = apk_path
        self.working_dir_path: str = working_dir_path
        self.output_apk_path: str = output_apk_path
        self.keystore_file: str = keystore_file
        self.keystore_passwd: str = keystore_passwd
        self.key_alias: str = key_alias
        self.key_passwd: str = key_passwd

        # check if specified APK is valid
        if not os.path.isfile(self.apk_path):
            print('Unable to find file "{0}"'.format(self.apk_path))
            raise FileNotFoundError('Unable to find file "{0}"'.format(self.apk_path))

        # if custom working directory is not specified, create a new directory "obfuscated_files"
        # in the same directory as the APK file
        if not self.working_dir_path:
            self.working_dir_path = os.path.join(
                os.path.dirname(self.apk_path), "obfuscated_files"
            )
            print(
                "No working directory provided, the operations will take place in the "
                'same directory as the input file, in the directory "{0}"'.format(
                    self.working_dir_path
                )
            )

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

        # if output path not specified, save in working directory
        if not self.output_apk_path:
            self.obfuscated_apk_path = "{0}_obfuscated.apk".format(
                os.path.join(
                    self.working_dir_path,
                    os.path.splitext(os.path.basename(self.apk_path))[0],
                )
            )
            print(
                "No obfuscated apk path provided, the result will be saved "
                'as "{0}"'.format(self.obfuscated_apk_path)
            )

        return

