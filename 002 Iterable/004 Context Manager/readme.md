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



