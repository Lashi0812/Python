print(f"{'-' * 25} Running {__name__} {'-' * 25}")


def pprint_dict(header, d):
    print("-" * 50)
    print(f"{'-' * 25} {header} {'-' * 25}")
    for k, v in d.items():
        print(k, v)
    print("-" * 50)


pprint_dict("module1.globals", globals())
print(f"{'-' * 25} END OF {__name__} {'-' * 25}")
