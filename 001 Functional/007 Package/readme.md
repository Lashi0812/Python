# Package are Module

1. Package are module but module not a package
2. Package contain
    1. module
    2. package (sub package)
3. if a module is a package , it must have a value set of ```__path__```

# Importing Nested package

```python
import pack.pack1.module
```

the import system wil perform the steps

```python
import pack
import pack.pack1
import pack.pack1.module1
```

the ```sys.modules``` cache will contain entries for:

```python
{
    "pack": < address1 >,
    "pack.pack1": < address2 >,
    "pack.pack1.module1": < address3 >
}
```

the namespace where the import was run contain:

```python
{
    "pack": < address1 >
}
```

# File based package

1. package paths are created by using files system directories and files
2. the *directory name* become the package name.
3. Since the package it just the folder cant contain the code for package.
   >    **Where does the code of the package goes?**
   >    1. code of the package in the **__init__.py**
      
   >    **What happen when a file based package is imported?**
   > ```python
   > app/
   >    pack1/
   >        __init__.py
   >        module1.py
   >        module2.py    
   > ```
   > ```python
   > import pack1
   > ```
   > 1. the code for te pack1 is in ```__init__.py```
   > 2. the code is loaded , executed and cached in ```sys.modules``` with a key of pack1
   > 3. the symbol pack1 is added to our namespace referencing the same object
   > 4. but it hae the ```__path__``` property ==> file system directory path
   > 5. also has a ```__file__``` property  ==> file path of *__init__.py*
   
