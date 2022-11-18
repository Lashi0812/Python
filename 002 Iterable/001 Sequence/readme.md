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