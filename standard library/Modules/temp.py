"""
Modules - it is a file containg python definations and statements(fnc., vars, classes)
Purpose:

Enable code reuse and organizations

Module -
 -> Built-in Modules: like math, os, sys, etc
 -> user Defined Modules: Custom pthon files with .py extension
 -> External Modules: Installed via pakacged managers(eg, numpy, pandas) (used via pip install command)

DEfination from a module can be imported into other modules or into the main module

Every module has a global variable __name__ as string
"""

## Module Search Path

"""
when you import a module in python using import module_name, python follows a specific
sequence to search for that module. This sequence of directories where Python looks for 
modules is called module path search
Default Seacrh Order:
-> Current Dir
-> Envirnment Variable PYTHONPATH
-> Thisd-Party Package Directory(site- packages)

"""
