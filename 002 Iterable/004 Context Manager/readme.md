<!-- TOC -->
* [Context Manager](#context-manager)
  * [Context Manager](#context-manager)
    * [Context Manager protocol](#context-manager-protocol)
    * [How Context Manager works](#how-context-manager-works)
    * [Scope of  with block](#scope-of--with-block)
    * [`__enter__` Method](#__enter__-method)
    * [`__exit__` Method](#__exit__-method)
      * [Scenario 1](#scenario-1)
      * [Scenario 2](#scenario-2)
* [Caveat with Lazy Iterator](#caveat-with-lazy-iterator)
  * [Solution](#solution)
* [Generator and Context Manager](#generator-and-context-manager)
  * [Context Manager Pattern](#context-manager-pattern)
  * [Mimic the Context Manager Using the Generator](#mimic-the-context-manager-using-the-generator)
  * [Creating the context manager from the generator function](#creating-the-context-manager-from-the-generator-function)
* [Decorating Generator Function](#decorating-generator-function)
<!-- TOC -->

# Context Manager

> What is context?
> * State surrounding the section of code

```python
# module.py
f = open("file.txt", "r")
print(f.readline())
f.close()
```

1. `print(f.readline())` runs , it has the context in which it runs,that *global scope*
2. When performing some operation with the file ,there could be exception occur before we close the file.

```python
f = open("file.txt", "r")
try:
    perform_work(f)
finally:
    f.close()   
```

this could avoid the problem of closing the file when the exception is raised.

## Context Manager

1. create the context with minimal amount of state needed for block of code.
2. execute some code with variable in the context
3. automatically clean up the context when we are done with it.
4. In simple word context manager manage the data in our scope.

### Context Manager protocol

Class implement the context manager protocol by implementing the two method.

| `__enter__` | setup and *optionally* return the object |
|-------------|------------------------------------------|
| `__exit__`  | cleanup activity                         |

```python
with CtxManager() as obj:
# do something
# done with context

# equivalent code
mgr = CntManager()
obj = mgr.__enter__()
try:
# do somthing 
finally:
    # done with context
    obj.__exit__()
```

### How Context Manager works

```python
class MyClass:
    def __init__(self):

    # init method
    def __enter__(self):
        return obj  # optional

    def __exit__(self, exc_type, exc_val, exc_tb):
# clean up obj
```

1. Context work along the `with` statement
2. `with MyClass() as obj`
    1. create the instance of the class , but *no symbol* is created in scope
    2. call `instance.__enter__()` and return optional object.
    3. if return the object we can catch the object using `as` keyword and the symbol is created in current scope.
    4. *return object is not instance of the MyClass*
3. after the with block finished or if exception is raised inside hte with block.
    1. instance.__exit__() is called.

### Scope of  with block

```python
with open("file") as f:
    row = f.readline()
print(f)
print(row)
```

`f` and `row` symbol exist in working namespace even after the with block is executed.

### `__enter__` Method

1. this method perform the setup operation for context
2. it can optionally return the object.

### `__exit__` Method

1. `__exit__` is similar to finally block , it will run even the exceptions is raised inside the with block.

```python
with MyContext() as obj:
    raise ValueError
print("done")
```

#### Scenario 1

* `__exit__` receive the error , perform the cleanup operation and *silence the error*
* print statement will run
* no exception is seen

#### Scenario 2

* `__exit__` receive the error , perform the cleanup operation and *lets error propagate*
* print statement will not run
* ValueError is seen

`__exit__` method take three argument

1. `exception type`
2. `exception value`
3. `trackback object`

Return True or False

* True --> Silence the error
* False --> propagate the error

# Caveat with Lazy Iterator

```python
def read_file():
    with open("test.txt", "r") as file:
        return file  # return lazy iterator


reader = read_file()
for row in reader:  # ValueError: I/O operation on closed file.
    print(row) 
```

When we exit the with block the file is close , we are trying to access the file. it throws error.

## Solution

```python
def read_file():
    with open("test.txt", "r") as file:
        yield from file  # yield lazy iterator


reader = read_file()
for row in reader:
    print(row)
    # print the row
```

Now there will no error ,since yield from don't close the file until we exhaust the file.

# Generator and Context Manager

## Context Manager Pattern

```python
with open("readme.md") as f:
    print(f.readline())
```

1. create the context manager
2. enter the context
3. do the stuff within the context
4. exit context

## Mimic the Context Manager Using the Generator

```python
def open_file(file_name, mode):
    # initialise
    f = open(file_name, mode)
    try:
        # similar __enter__ function
        yield f
    finally:
        # similar __exit__ function
        f.close()


# how to use this generator as the context manager
cxt = open_file("readme.md", "r")
f = next(cxt)  # open file and yield file
# do the stuff with file
next(cxt)  # close file
```

1. we can create the generator function
2. call the generation function
3. call the next on the generator which yield the opened file.
4. call again the next of the generator which close the file.

## Creating the context manager from the generator function

```python
class GenContexManager:
    def __init__(self, gen_fn, *args, **kwargs):
        self.gen = gen_fn(*args, **kwargs)

    def __enter__(self):
        return next(self.gen)

    def __exit__(self, exc_type, exc_val, exc_tb):
        next(self.gen)
        return False


with GenContexManager(open_file, file_name, mode) as file:
    print(file.read())
```

1. we are calling the generator function inside the init of context manager ,which create the generator object.
2. using with the GenContextManager we yield the object
3. we perform the task with that object
4. finally return exit the context manager
5. but we lost readability of code. `with open` tell we are opening something.
    1. but here `with GenContextManager` doesn't tell with what we are working.

# Decorating Generator Function

1. to fix readability issue we can decorator

```python
def context_manager_dec(gen_fn):
    def inner(*args, **kwargs):
        gen = gen_fn(*args, **kwargs)
        return GenContextManager(gen)

    return inner

@context_manager_dec
def open_file(file_name,mode):
    try:
        f = open(file_name,mode)
    finally:
        f.close()

with open_file(file_name,mode) as file:
    print(file.read())
```
Python implement these for us.
1. we don't need to write the generator context manager class.
2. we don't have to write the decorator
3. all we have to use the `contextmanager` decorator
```python
from contextlib import contextmanager

@contextmanager
def open_file(file_name,mode):
    try:
        f = open(file_name,mode)
        yield f
    finally:
        f.close()

with open_file("readme.md","r") as f:
    print(f.readlines())
```






