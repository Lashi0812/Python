# Constructing the instance of class
1. `object` class implement the `__new__` method.
2. it is default implementation of `__new__` and used to creation of *instance of any class.*
3. we can call directly 
    ```pycon
    >>> class Person:
    ...     def __init__(self,name):
    ...         self.name = name
    ... 
    >>> p = object.__new__(Person)
    >>> type(p) , p 
    (<class '__main__.Person'>, <__main__.Person object at 0x0000013A63344850>)
    ```
4. `__init__` is not called. we have to do it ourselves
   ```pycon
   >>> p.__init__("A")
   >>> p
   <__main__.Person object at 0x0000013A63344850>
   >>> p.__dict__
   {'name': 'A'}
   ```
5. `__new__` is a static method. that is this method not bound to any object.
6. signature must match the `__init__` signature.
7. it may or may not return the instance of the class

## Overriding the `__new__` method
1. we usually delegate the instance creation to the `object` class.
2. we just perform the task that need to do `before or after` the creation of the instance.

```python
class Person:
    def __new__(cls, *args, **kwargs):
        # task before the creation
        
        #creating the instance
        instance = super().__new__(cls)
        
        #task after the creation
        
        #return the instance
        return instance 
```

# How classes are created?
## Overview:
1. When python encounter the `class keyword` as it complies our code
   ```python
   class Person:
       pass
   ```
2. a symbol `Person` is created in the namespace.
   ```pycon
   >>> globals()
   {'Person': <class '__main__.Person'>}   
   ```
3. that symbol is a `reference` of the *class Person* it is an object.
4. a *class* is an `instance of type`
   ```pycon
   >>> type(Person)
   <class 'type'>   
   ```
5. that why we call the class as a type.
6. type class `inherit object class`
   ```pycon
   >>> isinstance(type,object)
   True
   ```

## Inner mechanic of class creation:
```python
class Person:
    planet = "Earth"
    galaxy = "Milky Way"
    
    def __init__(self):
       pass      
```
1. the class body is extracted.
2. a *new dictionary* is created - this will be `namespace` of  new class
   ```pycon
   >>> namespace = {}
   ```
3. the class body is executed inside the namespace. thereby populating the namespace.
4. A new *type class instance* is created using the name of class,base class and populated dictionary
   ```pycon
   >>> type('Person',(object,),namespace)       
   <class '__main__.Person'>
   ```

# Inheriting from type:
refer the notebook

# Metaclass
1. class which used to create the other class are called metaclass.
2. by default python use the `type class` as the metaclass.
   ```python
    class Person(metaclass=type):
        pass
   ```
3. we can override this.
   ```python
   class Person(metaclass=Mytype):
       pass
   ```
