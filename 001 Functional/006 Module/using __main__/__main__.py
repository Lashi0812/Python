print(f'loading run.py: __name__ = {__name__}')
import timer

result = timer.timeit('list(range(1_000_000))', repeats=20)
print(result)