# The Best Smali Code Obfuscator
> An ICT2207 Mobile Security Project done by P6 Team 2 (AY2021/2022)

**The Best Smali Code Obfuscator** is a python-based application that takes in an Android Package (APK) file for disassembly into smali code. The algorithms we’ve derived in the application will then transform and obfuscate the smali files, before it is resigned and built into an obfuscated APK file. The application relies on an external tool called Apktool to decompile the APK files into smali files before they can be obfuscated. Afterwhich, another tool, called apksigner, is called and utilised to rebuild and sign the obfuscated apk file.

The obfuscation algorithms that we’ve derived can be separated into 5 distinct obfuscators that work well by itself and as good together. These 5 obfuscators are given the following names:

 1. NOP obfuscation
 2. Random_manifest obfuscator
 3. Goto obfuscator
 4. Opaque predicates
 5. Junk Code
 
## > Prerequisites
### >> Python Packages
Ensure to have the following python packages installed:
 - [pyside2](https://pypi.org/project/PySide2/) & [pyqt5](https://pypi.org/project/PyQt5/)
	 - Official Python module for Qt framework. Utilised in creating GUIs for python applications to run on.
	 - PySide2~=5.15.2.1
	 - PyQt5~=5.15.6Q
 - [qdarkstyle](https://pypi.org/project/QDarkStyle/)
	 - Utilised in dark style mode for Qt applications.
	 - DarkStyle~=3.0.3
 - [python-magic-bin](https://pypi.org/project/python-magic-bin/)
	 - Used in identifying file types of a given file, MIME-type output.

### >> External Tools
Ensure to have the following tools & files found in the [**tools**](https://github.com/clamismagic/ict2207-coursework2/tree/main/tools) folder:
 - apksigner.bat
 - apktool.bat
 - apktool.jar
 - libs_to_ignore.txt
 - /lib/apksigner.jar

# > Usage
To use the application, run the **designer_ui.py** file with a Python interpreter.

![](https://cdn.discordapp.com/attachments/824412859706376232/959290286322888704/unknown.png)

Browse for an APK file you wish to obfuscate by selecting the Browse Button.

![](https://cdn.discordapp.com/attachments/824412859706376232/959290760518316104/unknown.png)

Hit the Obfuscate button. The application will down decompile, and obfuscate the AndroidManifest.xml file and all Smali files.

![](https://cdn.discordapp.com/attachments/824412859706376232/959290997702025296/unknown.png)

You are also able to view the original and obfuscated Smali file by selecting the file on the left List Widget.

![](https://cdn.discordapp.com/attachments/824412859706376232/959291522300399656/unknown.png)

To Sign & Build the file, browse for the key file you wish the utilize for signing, and the password. Hit the Build & Sign Button whenever you are ready to build & sign the APK.

![](https://cdn.discordapp.com/attachments/824412859706376232/959291961439834112/unknown.png)
