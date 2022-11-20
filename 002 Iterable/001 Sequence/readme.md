<!-- TOC -->
* [What is Sequence?](#what-is-sequence)
* [Builtin sequence Types](#builtin-sequence-types)
* [Other sequence type in Collection package](#other-sequence-type-in-collection-package)
* [Homogenous and Heterogeneous Sequence](#homogenous-and-heterogeneous-sequence)
* [Iterable vs Sequence](#iterable-vs-sequence)
* [List vs Tuple](#list-vs-tuple)
  * [Creating](#creating)
  * [Coping](#coping)
  * [Storing](#storing)
* [Custom Sequence](#custom-sequence)
  * [`__getitem__`](#__getitem__)
  * [`__add__`](#__add__)
  * [`__iadd`](#__iadd)
  * [`__mul__`](#__mul__)
  * [`__imul__`](#__imul__)
  * [`__rmul__`](#__rmul__)
  * [`__setitem__`](#__setitem__)
  * [`__contains__`](#__contains__)
  * [`__delitem__`](#__delitem__)
* [Inplace concatenation and repetition](#inplace-concatenation-and-repetition)
* [Comprehension](#comprehension)
  * [Scope](#scope)
<!-- TOC -->

# What is Sequence?
1. sequence of element with *positional ordering*
2. indexing start from 0

# Builtin sequence Types
1. ```mutable``` -> lists, bytearrays
2. ```immutable``` -> string,tuple,range,bytes

# Other sequence type in Collection package
1. namedtuple
2. deque
3. array

# Homogenous and Heterogeneous Sequence
1. ```Homogeneous``` each element have same type , it is more efficient than the heterogeneous
2. ```Heterogeneous``` each element have different type

# Iterable vs Sequence
1. ```iterable``` is a container type of object, and we can list out the element in that object *one by one.*
2. sequence is a iterable
3. iterable is not sequence
4. ```set``` is iterable but not sequence.

# List vs Tuple

## Creating

> Constant folding is the process of recognizing and evaluating constant expressions at compile time rather than computing them at runtime

1. if we have container containing only constant element we don't change the element in the container then creating the tuple is much faster than list
2. because tuple container as a single constant
3. but in case of list each element is separate constant, load them separating and finally create the list

## Coping
1. shallow coping the tuple faster the shallow copying the list
2. because in tuple copy element will have the same address of the original tuple
3. in list both will have different address.

## Storing
1. When mutable container objects such as lists, sets, dictionaries, etc are created, and during their lifetime, the allocated capacity of these containers (the number of items they can contain) is greater than the number of elements in the container. This is done to make adding elements to the collection more efficient, and is called over-allocating.
2. Immutable containers on the other hand, since their item count is fixed once they have been created, do not need this overallocation - so their storage efficiency is greate


# Custom Sequence
1. If object said to be sequence then the class should have implement two method  ```__len__ ,__getitem__```
2. ```__len__``` return the length of that sequence 
3. ```__getitem__``` return the element at an index in the sequence
4. If an object have these functionality we can use the ```[]``` and ```for``` in the sequence

## `__getitem__`
1. it returns the element in the sequence at the requested index or raise IndexError when index is out of bound
```python
for item in my_list:
    print(item**2)

# equivalent way is 
index = 0 
while True:
    try:
        item = my_list.__getitem__(index)
    except IndexError:
        break
    print(item **2)
    index +=1
```

## `__add__`
concat the two same type of sequence.
```python
l = [1,2,3,4]
l1 = [5,6]
l + l1

# equivalent way
l.__add__(l1)
```

## `__iadd`
inplace concat the calling object should implement this method and take the argument of *iterable*
```python
l = [1,2,3,4]
l1 = [5,6]
l += l1

# equivalent way
l.__iadd__(l1)
```

## `__mul__`
reputation of sequence argument should be integer . return the new object 
```python
l = [1,2,3,4]
l * 2 

# equivalent way
l.__mul__(2)
```

## `__imul__`
inplace reputation , mutate the same object
```python
l = [1,2,3,4]
l *= 2 

# equivalent way
l.__imul__(2)
```

## `__rmul__`
now the calling object is integer and the argument is sequence type.
since , the integer class don't implement this functionality, raise the type error, the python try to call 
```l.__rmul__(2)```
```python
l = [1,2,3,4]
2 * l

# equivalent way
l.__rmul__(2)
```

## `__setitem__`
like getting the element from the sequence wwe can also set the element in the sequence by implementing the `__setitem__`.

## `__contains__`
we use the `in` operator to check the element presence in the list

## `__delitem__`
we use the `del` keyword to delete element in the sequence




# Inplace concatenation and repetition
1. `+=` operator will do the inplace concatenation.
2. `*_` operator will do inplace repetition.
3. inplace operator work for mutable sequence and object is mutated.
4. inplace operator work for immutable sequence and object don't mutated will produce the new object.

# Comprehension
1. Comprehension have their *own local scope* - just like a function.
2. ```rhs=[i**2 for i range(10)]``` and ```sq=rhs```
3. when we complied the rhs :Python create temporary function that used to evaluate the comprehension
    ```python
    def temp():
        new_list = []   
        for i in range(10):
            new_list.append(i**2)
        return new_list
    ```
4. When the line execute : Execute the temps and store the returned object in memory and finally `point sq to that object`

## Scope
1. they can access the global variable
    ```python
    num = 100
    sq = [i**2 for i range(num)]   
    ```
2. they can access the nonlocal scope.
    ```python
    def my_fnc(num):
        sq = [i**2 for i range(num)]   
    ```


