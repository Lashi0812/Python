# Iterating Sequence

1. When the sequence has the positional ordering, we cna iterate over that sequence using the index of the sequence.
2. `__getitem__` method in python help to do iteration over the sequence.

# Iterable

1. Since the sequence has the index we iterate over that sequence container.
2. there are other container that don't have the positional ordering like set. but still its container
3. Since all container have the element in them , we should have the concept the taking element from the container. Just
   like *marble in the container jar*
4. container which have concept taking one element from the container are called *iterable*.

## concept of next

1. for iterable we need just element the container.
2. *But how we know the exhaust the container, or we need to stop taking the element from the container?*
    1. When all the element in the container are taken out we have to return the ```StopIteration```.this tell us all
       the element is exhausted.
    2. we have same concept when we are iterating over the sequence container . there we return ```IndexError```

## building the iterable

1. for implement the iterable we need concept of next item

```python
class Container:
    def __init__(self):
        self.i = 0

    def next(self):
        result = self.i
        self.i += 1
        return result


container = Container()
for _ in range(5):
    print(container.next())
```

This implication of iterable have issues

1. the container is infinite
2. cannot restart the iteration *from the beginning*.
3. cannot use a for loop , comprehension

### Finite container

1. we specify the number of element in container when we are creating the container
2. we *raise StopIteration* if we ran out of element in container.

```python
class Container:
    def __init__(self, total):
        self.i = 0
        self.total = total

    def next(self):
        if self.i >= self.total:
            raise StopIteration
        result = self.i
        self.i += 1
        return result


container = Container(5)
while True:
    try:
        item = container.next()
        print(item)
    except StopIteration:
        break
```

### `__next__`

1. similar to len function , python has the special method ```__next__```

```python
class Container:
    def __init__(self, total):
        self.i = 0
        self.total = total

    def __next__(self):
        if self.i >= self.total:
            raise StopIteration
        result = self.i
        self.i += 1
        return result


container = Container(5)
while True:
    try:
        item = next(container)
        print(item)
    except StopIteration:
        break
```

# Iterator

1. We created a custom container type object with a `__next__` method
2. But it had several drawbacks
    1. cannot use a for loop
    2. once we start using next there's no going back
    3. once we have reached StopIteration we're basically done with the object

## Handle loop issue

1. we need to tell Python that our class has that `__next__` method and that it will behave in a way consistent with
   using a while loop to iterate.
2. Python knows we have `__next__`, but how does it know we implement StopIteration?

### Iterator Protocol

1. the class needs to implement two methods:
    1. `__next__` -> responsible for handing back the next element from the container and raising the `StopIteration`
       exception when all element have been handed out.
    2. `__iter__` -> just return the object itself.

```python
class Container:
    def __init__(self, total):
        self.i = 0
        self.total = total

    def __next__(self):
        if self.i >= self.total:
            raise StopIteration
        result = self.i
        self.i += 1
        return result

    def __iter__(self):
        return self


container = Container(5)
for item in container:
    print(item)
```

### How Python does?

1. call the `iter(iterable)` and store it `some instance`
2. call the `next(some instance)` until get the `StopIteration exception`

```python
container = Container(5)
cont_iter = iter(container)
while True:
    try:
        item = next(cont_iter)
        print(item)
    except StopIteration:
        break
```

Still we have one issue . the iterator cannot be restarted

# Iterator and Iterables

## Iterator

We saw that an iterator is an object that implement two methods.

| `__iter__` | return the object itself |
|------------|--------------------------|
| `__next__` | return the next element  |

1. The drawback is that iterator get *exhausted*
    * become useless for iterating again
    * become throw away objects

2. to iterator again collection we need to recreate them.

3. But two distinct thing is going on
    1. maintaining the container
    2. iterator over the container

**Why should we have to re-create the container just to iterate over them?**

## Separating the collection from the iterator

1. Instead , we would prefer to separate these two
    * maintain the container as the separate object (**Iterable**)
    * iterating over the container should be separate object.(**Iterator**)
2. Iterable is *created once*
3. Iterator is *created every time* we need to iterator the iterable

```python
class Cities:
    def __init__(self):
        self._cities = ["A", "B", "C", "D"]
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._cities):
            raise StopIteration
        else:
            item = self._cities[self._index]
            self._index += 1
            return item
```

1. Cities instances are **iterator**
2. Every time we want to run a **new loop**, we have to create a **new instance of Cities**
3. This is wasteful, because we should not have to **re-create the _cities** list every time

```python
class Cities:
    def __init__(self):
        self._cities = ["A", "B", "C", "D"]

    def __len__(self):
        return len(self._cities)


class CityIterator:
    def __init__(self, cities):
        self._cities = cities
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._cities):
            raise StopIteration
        else:
            item = self._cities[self._index]
            self._index += 1
            return item    
```

We have seperated the container and Iterator as separate object.

```python
cities = Cities()
cit_iteraror = CityTrerator(cities)
for city in cit_iteraror:
    print(city)
```

if we want to re-iterator the cities , now we need just re-creator the iterator object **not the container itself**

```python
cit_iteraror = CityTrerator(cities)
for city in cit_iteraror:
    print(city)
```

**What we have done so far?**

1. we have container that hold the element
2. a separate object , the iterator used to iterator over the collection.
3. But we have to **remember to create new iterator** to iterate the container.
4. But we want python to automatically create the new iterator we need to iterate the container.

## Iterable

1. Iterable is an object that implement `__iter__` that return the **new instance of the iterator** object used to
   iterate over the iterable.

```python
class Cities:
    def __init__(self):
        self._cities = ["A", "B", "C", "D"]

    def __len__(self):
        return len(self._cities)

    def __iter__(self):
        return CityIterator(self._cities)
```

Now we don't need the iterator object every time we need to iterate the iterable.

# Iterable vs Iterator

An **iterable** is an object that implements

| `__iter__` | return the iterator,(new instance) |
|------------|------------------------------------|

An iterator is an object that implement

| `__iter__` | return itself       |
|------------|---------------------|
| `__next__` | return next element |

# For Loop

* Python check object that implement the iter method if it does then for loop is done via the iterable protocol.
* if not then check fot getitem , it if it has , then for loop done via the sequence protocol.
* if it does not have both iter and getitem then throw error.






