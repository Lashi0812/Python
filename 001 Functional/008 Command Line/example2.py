import sys

numbers = (int(e) for e in sys.argv[1:])
print(sum(numbers))
