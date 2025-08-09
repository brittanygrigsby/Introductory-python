#Python Collections
#A group of data elements in python that allow us to store multiple
#data in a single variable

#1. Lists - They're used to store multiple items in a single variable
#and they use square brackets
# Properties: lists are ordered, changeable (or multiple) and allow duplixates
empty_list = [] #This is an empty list
print(f"Collection Data type: {type(empty_list)}")#Data type

fruits_list = ["apple","banana","cherry","orange","grapes"] #This is a list with default values
#                0        1       2         3        4
print(f"Empty List: {empty_list}")
print(f"List: {fruits_list}")
print(f"Retrieving a value: {fruits_list[0]}")
print(f"List length: {len(fruits_list)}")
print(f"Accessing Elements by Negative Indexing: {fruits_list[-1]}")
print(f"Accessing Elements by ranges[n:n]: {fruits_list[0:3]}")

# [a:b] where "a" is the starting index in the array (included) and "b" is the stopping point (exlcuding from list)
print(f"Accessing Elements by ranges[:n]: {fruits_list[:2]}")
print(f"Accessing Elements by ranges[n:]: {fruits_list[2:]}")

#Adding elements to the list
fruits_list.append ("watermelon")
fruits_list.append("strawberry")
print(f"Adding elements: {fruits_list}")


#Remove elements from the list
# fruits_list.pop(4)
fruits_list.pop()
print(f"Removing element from list: {fruits_list}")
fruits_list.remove("banana")
print(f"Removing element from list using remove method: {fruits_list}")
fruits_list.insert(0, "pear")
print(f"Using insert method: {fruits_list}")
fruits_list[2] = "blueberry"
print(f"Changing actual values: {fruits_list}")

#2. Dictionary
#Are use to store data values in key: value pairs.
#properties: ordered, changeable and do not allow duplicates
my_dictionary = {
    "brand":"Ford",
    "model":"Mustang",
    "year":1964,
    "color":["red", "white", "blue", "black"]
}
print(f"---------Dictionaries-----------")
print(f"Dictionary: {my_dictionary}     |    Type: {type(my_dictionary)}")
print(f"Accessing items using keys: {my_dictionary['year']}")
print(f"Dictionary length: {len(my_dictionary)}")
print(f"Accessing items using get: {my_dictionary.get("brand")}")
print(f"Only print the keys: {my_dictionary.keys()}")
print(f"Only print the values: {my_dictionary.values()}")
#my_dictionary ["year"] = 1984
my_dictionary.update({"year":1985})
print(f"Modifying the dictionary: {my_dictionary}")
my_dictionary.pop("colors")
print(f"Deleting elements: {my_dictionary}")
#3. Tuples
#Store multiple items in a single variable
#Properties: ordered and unchangeable
print(f"--------Tuples---------")
my_tuple = ("apple","banana","cherry")
print(f"Tuple:{my_tuple} | Data type: {type(my_tuple)}")
print(f"Accessing elements: {my_tuple[2]}")
modified_tuple = list(my_tuple)
modified_tuple.append("Watermelon")
modified_tuple.pop(0)
my_tuple = tuple(modified_tuple)
print(f"Tuple: {my_tuple} | Data type: {type(my_tuple)}")