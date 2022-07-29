# Python-Awesome-Module-Importing-System
A lightweight, simple way to import python modules with error-handling and auto-installation

# Features:
- Error-handling for module not found errors
- Auto-installation of modules via pip system
- Can be set to terminate or warn if a module cannot be installed
- Creation of variables so you can check if a module has been installed
(EX: calling `importmodule("io")` will create a global variable `ioimported` with the value `True` or `False`)
- Simple to use - just copy and paste this code to the top of your program, and use `importmodule("modulename")` to import modules
- High compatibility - no modules need to be installed beforehand for this system to work, as only default modules are used
- Install once, use forever - once a module is successfully installed with this system, the module will be recognized the next time it is imported, whether will this system or with the default `import module` system

# Usage:
1. Paste the code at the top of your program
2. Use `importmodule("modulename")` to import modules
Note that using this function will create variables so you can check if a module has been installed
(EX: calling `importmodule("io")` will create a global variable `ioimported` with the value `True` or `False`)

# Syntax:
Arguments to the `importmodule` function:
1. Module Name: Required argument. Accepts a string that is the name of the module you want to import. EX: "io"
2. Terminate: Not required. Accepts a bool value that tells the program whether to terminate or not if the module cannot be imported. Default `True`

# Requirements:
As stated earlier, I believe the system is compatible with all versions of python with no setup needed! Please correct me if I am wrong.
