#   Created by Elshad Karimov on 20/04/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

#  Update / add an element to the dictionary

myDict = {'name': 'Edy', 'age': 26}
myDict['address'] = 'London'
print(myDict)

#  Traverse through a dictionary

def traverseDict(dict):
    for key in dict:
        print(key, dict[key])

traverseDict(myDict)

#  Searching a dictionary


def searchDict(dict, value):
    for key in dict:
        if dict[key] == value:
            return key, value
    return 'The value does not exist'
print(searchDict(myDict, 27))

#  Delete or remove a dictionary

myDict.pop('name')

# sorted method
myDict = {'eooooa': 1, 'aas': 2, 'udd': 3, 'sseo': 4, 'werwi': 5}

print(sorted(myDict, key=len))

# Methods

myDict2 = myDict.copy()
myDict2.clear()

newDict = {}.fromkeys([1,2,3,4], 0). # Sets 4 keys 1,2,3,4 and assigns them to value 0.
myDict.get("age",27) # Returns value of age if it exist in myDict or assigns a default value of 27
newDict.items() # Return key, value pair in a tuple format inside a list.
newDict.keys() # Returns all keys in a list
newDict.values() 
newDict.popitem() # Deletes the last item and returns it
newDict.setdefault("name", 3) # Returns value of key if it exists or adds the key to the end.
newDict.update(myDict) # Takes another dictionary as parameter. Updates the values of key if they alredy exist or it adds it to the end of dictionary

