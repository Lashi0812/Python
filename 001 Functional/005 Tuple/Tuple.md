**Tuple vs List vs string**

| Tuple         | String      | List          |
|---------------|-------------|---------------|
| container     | container   | container     |
| order matter  | order mater | order matter  |
| *Hetero*/Home | *Homo*      | Hetero/*Home* |
| indexable     | indexable   | indexable     |
| iterable      | iterable    | iterable      |
| immutable     | immutable   | *mutable*     |

**Immutable of Tuple**
1. element cannot be added or removed
2. the order of element  cannot be changed
3. *work well for representing data structure*
    * Point(x,y)
    * Circle(x,y,radius)
    * City(city,country,pop)
4. position of data has meaning
5. Without creating the class we can create different data structure

**Named Tuple**
1. To give the name of element in tuple we may try to create the class for the 
2. When we create the instance of the object is mutable
3. But in class approach the code become more robust . we will unpack the using the field name.
4. WE combine the tuple and class 
5. tuple is mutable and class give the meaningful name to position
6.  ```from collection import namedtuple``` will have this property.
7. namedtuple is function which generate a new class, so it is called as*class factory*
8. that new class inherit from tuple

**Generating Named Tuple class**
1. namedtuple is a class factory
2. it creates a new class which inherit the tuple
3. to generate this class we need
   * class name
   * filed names
4. return value of this function is class
```python
from collections import namedtuple
Point2D  = namedtuple("Point2D",[x,y])
```
1. different way to provide the list of field names
   * list of string
   * tuple of string
   * a string separated by comma or space

**Accessing Data in a namedtuple**
1. since this class is the instance of tuple
   * by index
   * slice
   * iterate
   * unpacking
2. since named tuple is class
   * by field names
3. **instance and attribute is immutable**