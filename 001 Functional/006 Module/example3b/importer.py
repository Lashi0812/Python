import os.path
import types
import sys


print("Importer.py")

def import_(module_name, module_file, module_path):
    if module_name in sys.modules:
        return sys.modules[module_name]

    module_rel_path = os.path.join(module_path, module_file)
    module_abs_path = os.path.abspath(module_rel_path)

    # read the source code from the file
    with open(module_abs_path, 'r') as code_file:
        source_code = code_file.read()

    # create the module
    mod = types.ModuleType(name=module_name)
    mod.__file__ = module_abs_path

    # set the ref in the sys module
    sys.modules[module_name] = mod

    # compile source code
    code = compile(source_code, filename=module_abs_path, mode="exec")

    # exec compile source code
    exec(code, mod.__dict__)

    return sys.modules[module_name]
