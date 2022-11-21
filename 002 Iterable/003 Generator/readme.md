# Generator

1. Generator function are function which contain at least on *yield* statement.
2. when the generator function is called ,python *create a generator object*.
3. generator implement the *iterator protocol*.
4. Generator are inherently *lazy iterator*.
5. Generator become exhausted once the function return a value.

# Making an Iterable from the generator

1. Generator are iterator
    1. they become exhausted
    2. they cannot be restarted
2. This may lead to bug if we try to iterate twice over the generator.

```python
def squares(n):
    for i in range(n):
        yield i ** 2


sq = squares(5)
l = list(sq)
l = list(sq)  # empty list
```

To make the generator into iterable

```python
class Squares:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return squares(n)


sq = Squares(5)
```

# Delegating to another iterator

```python
def read_all_data():
    for file in ('file1.csv', 'file2.csv', 'file3.csv'):
        with open(file) as f:
            for line in f:
                yield line
```

The inner loop is basically just using the file iterator and yielding value directly. We are delegating the yielding to
the file iterator

We can replace this inner loop by `yield from`

```python
def read_all_data():
    for file in ('file1.csv', 'file2.csv', 'file3.csv'):
        with open(file) as f:
            yield from f
```



