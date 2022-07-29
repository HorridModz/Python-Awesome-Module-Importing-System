#   Modules required for importing other modules

import sys
import warnings
import importlib
import pip

#   Importing Modules

def modulenotfounderror(module,terminate = True):
    print("Could not import module '" + module + "'.\
\nSome features may not work or give errors due to this module not being installed.")
    TRY_INSTALL = input("Would you like to try to install the module? An internet connection is required to do so.\nY\\N\n")
    if TRY_INSTALL == "Y" or TRY_INSTALL == "y":
        if not(install_and_import(module)):
            print("\n\nSuccessfully installed and imported module '" + module + "' !")
        else:
            globals()[module + "imported"] = False
            if terminate:
                sys.exit()
    else:
        globals()[module + "imported"] = False
        print("Could not import module '" + module + "'.")
        if terminate:
            sys.exit()
def install_and_import(module):
    INSTALL_ERROR = False
    try:
        importlib.import_module(module)
    except ImportError:
        try:
            import pip
            pip.main(['install', module])
        except:
            INSTALL_ERROR = True
        finally:
            if not(INSTALL_ERROR):
                try:
                    globals()[package] = importlib.import_module(module)
                except:
                    INSTALL_ERROR = True
                    print("\n\nFailed to install module '" + module + "' due to unknown reason. Check that you have an internet connection and that your disk is not full.")
            return(INSTALL_ERROR)

def importmodule(module,terminate = True):
    globals()[module + "imported"] = True
    try:
        importlib.import_module(module)
    except ImportError:
        modulenotfounderror(module,terminate)
        
#Comment out these examples and try them one by one!
        
importmodule("io",True) #Import default module and terminate if install failed
importmodule("io",False) #Import default module and warn if install failed
importmodule("discord",True) #Import non-default module and terminate if install failed (change this to a non-default module you do not already have installed to test)
importmodule("discord",False) #Import non-default module and terminate if install failed (change this to a non-default module you do not already have installed to test)
importmodule("Modulethatdoesnotexist",True)  #Import nonexistent module and terminate if install failed (for testing purposes only)
importmodule("Modulethatalsodoesnotexist",False) #Import nonexistent module and warn if install failed (for testing purposes only)
