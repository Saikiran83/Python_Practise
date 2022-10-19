# JSON stands for JavaScript Object Notation, and is a file format that stores data. JSON files are basically like python dictionaries, but on steroids. They help in storing data and enable communication with servers during deployment. Oftentimes a single programming language is not enough to solve a problem, and json objects act as a bridge between them.
# JSON Objects	Python Equivalent
# Object	     Dictionary (dict)
# Array	         List (list)
# String	     String (str)
# Number	     Integer (int), Float (float)
# Boolean true	 True
# Boolean false	 False
# Null	         None
# Python's json module:
# As the part of programming, it is very common requirement to convert python object into 
# json form and from json form to python object. For these conversions (Serialization and 
# Deserialization) Python provides inbuilt module json.
# json module defines the following important functions:

# For Serialization Purpose (From Python to JSON Form):
# 1) dumps()  It serializes python dict object to json string.
# 2) dump()  Converting python dict object to json and write that json to provided json 
# file. It serializes to a file.

# For Deserialization Purpose (From JSON form to Python form):
# 1) loads()  Converting JSON string to python dict. It deserializes to a string.
# 2) load()  Reading json from a file and converting to python dict object. Deserializes 
# from a json file.
