# Create a HashMap with at least 10 key value pairs of the Student ID and Name
# Insert a Key value mapping into the map
# Fetch the value of a Key
# Create a clone/copy of HashMap
# Check if the given Key is in the Map
# Check if the value is in the Map
# Check if the map is empty
# Print the size of the Map to the console
# Print all the Keys of the map to the console
# Print all the Keys of the map to the console
# Remove a specific Key-value pair
# Copy all the elements of the Map to another Map



students = {1:'arun',2:'anil',3:'shobha',4:'nath',5:'kanth'}

def insert(key,value):
    students[key] = value
def get(key):
    return students[key]

def copy():
    dic = dict(students)

def check_key(a):
    return a in students

def check_value(a):
    return a in students.values()

def check_empty(a):
    return {} == a

def length(a):
    return len(a)

def keys(a):
    return a.keys()

def values(a):
    return a.values()

def remove(a):
    students.pop(a)
    

