# Class and Instance

## Namespace

* Class and its instance will have **distinct namespace**.
* Even though **Class itself instance of Object Class**
* type of Class namespace is *mappingproxy* read only dict.
* type of Instance namespace is *dict* , so we can modify directly namespace.

```python
class MyClass(object):
    language = "python"


instance = MyClass()
MyClass.__dict__  # Class namespace{"language" : "python"}
instance.__dict__  # instance namespace is empty{}
```

## Data Attribute

```pycon
class MyClass:
    language = "python"


instance = MyClass()
MyClass.__dict__  # Class namespace{"language" : "python"}
instance.__dict__  # instance namespace is empty{}

MyClass.language  # pyhton
instance.language  # python
```

1. when we search the language attribute in the *class namespace* `Myclass.language` python is find the attribute
   in `Myclass object namespace` return the value.
2. when we search the language attribute in the *instance namespace* `instance.language` python *does not find the
   language attribute in instance object*
    1. So python goes up and search in the *class namespace* and find it return the value.



```python 
class MyClass:
    language = "python"  # (class atrribute)


instance = MyClass()
MyClass.__dict__  # Class namespace {"language" : "python"}
instance.__dict__  # instance namespace is empty{}

MyClass.language  # pyhton 
instance.language = "jave"  # (instance atrribute)
instance.__dict__  # instance namespace is empty {"language" : "java"}
instance.language  # java
```

1. when we search the language attribute in the *class namespace* `Myclass.language` python is find the attribute
   in `Myclass object namespace` return the value.
2. when we search the language attribute in the *instance namespace* `instance.language` python *now find the
   language attribute in instance object* , so return value.


