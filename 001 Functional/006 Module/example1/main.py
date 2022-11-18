import sys
from ctypes import c_long

print("-" * 75)
print(f"{'-' * 25} Running {__name__} {'-' * 25}")
import module1

print(module1)
module1.pprint_dict("main.globals", globals())

print(sys.path)
print(c_long.from_address(id(module1)).value)

idx = id(module1)

print("deleting the reference form the global namespace")
del globals()["module1"]
print(c_long.from_address(idx).value)

print("Trying to import again the module1 ")
import module1


print("deleting the reference form the sys module namespace")
del sys.modules["module1"]
print(c_long.from_address(idx).value)


print("Trying to import again the module1 ")
import module1


print("-" * 75)
