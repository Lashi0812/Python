"""
Times the conde snippet how long it take to run over multiple iteration
"""

from time import perf_counter
from collections import namedtuple
import argparse

Timing = namedtuple("Timing", "repeats elapsed average")


def timeit(code, repeats):
    code = compile(code, filename="<string>", mode="exec")
    start = perf_counter()
    for _ in range(repeats):
        exec(code)
    end = perf_counter()
    elapsed = end - start
    avg = elapsed / repeats
    return Timing(repeats, elapsed, avg)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("code", type=str, help="The Python code snippet to timed")
    parser.add_argument("-r", "--repeats", default=10, type=int, help="Number of time to repeats test")
    args = parser.parse_args()
    print(f"timing {args.code}...")
    print(timeit(code=args.code, repeats=args.repeats))
