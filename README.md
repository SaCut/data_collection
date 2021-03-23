# Lists and Tuples

### What is a list?
- A list is a collection of elements
- Lists in Python are mutable
- The syntax `list_name = []` is used to create a list
- In Python, lists can contain different data types

### List methods
- Indexing
- `list_name[0]` gives back the 0th value in list

- Changing an item
- `list_name[0] = "element"` changes the 0th value to something different

- Adding an item
- `list_name.append(variable)` adds an element to the end of the list

- Removing an item
- `list_name.remove("element")` or `list_name.remove(list_name[0])` removes the specified element from the list

#### What is a tuple?
- A tuple is also a collection of elements
- In contrast to lists, tuples are immbutable once created
- The syntax `tuple_name = ()` is used to create a tuple
- Tuples can also contain different data types

### What is a dictionary?
- A dictionary is another collection of elements
- Dictionaries hold a collection of keys, and each key can have an assigned value
- The syntax `dict_name = {"key": "value"}` is used to create a dictionary
- Dictionary can contain any data type, including lists and tuples

#### Dictionary methods
- `dict_name["key"]` gives back the values associated with that key
- `dict_name.keys()` gives back all the keys in a dictionary
- `dict_name.values()` gives back all the values in a dictionary

### Sets
- Sets are data collections like lists, tuples and dictionaries, but they are not ordered
- The syntax `set_name = {"element1", "element2", "element3"}` is used to create a set
- Sets are mutable

#### Sets methods
- add
- discard