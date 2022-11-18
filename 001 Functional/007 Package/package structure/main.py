import common.validator

common.validator.is_json({})


print("*" * 20 + "   self    " + "*" * 20)
for k in dict(globals()).keys():
    if str(k).startswith("__"):
        continue
    print(k)

print("*" * 20 + "   common    " + "*" * 20)
for k in common.__dict__.keys():
    if str(k).startswith("__"):
        continue
    print(k)

print("*" * 20 + "   validator    " + "*" * 20)
for k in common.validator.__dict__.keys():
    if str(k).startswith("__"):
        continue
    print(k)

print("*" * 20 + "   numeric    " + "*" * 20)
for k in common.validator.numeric.__dict__.keys():
    if str(k).startswith("__"):
        continue
    print(k)
