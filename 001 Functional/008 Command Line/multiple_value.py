import argparse

parser = argparse.ArgumentParser(description="concat two list")
parser.add_argument("-1", help="list one", type=int, nargs="*", required=True, dest="first")
parser.add_argument("-2", help="list two", type=int, nargs="+", required=True, dest="second")
args = parser.parse_args()
print(args.first + args.second)
