# Problem 2
# Open example.json with the json.loads( ) function and using it, create a new json file that stores only the mappings between the students’ names and their phone numbers.
import json
with open("example.json", "r") as file:
    fileData = file.read()
    json_data = json.loads(fileData)
phoneRecord = {}
for name in json_data:
    phoneRecord[name] = json_data[name]["number"]
with open("output.json", "w") as outputFile:
    json.dump(phoneRecord, outputFile)
print("Process Complete!")

# Algorithm:

# Load the json file into a file object and read its contents with the file.read() function, which returns a string containing the file’s contents.
# Use the json.loads() function to convert this string object into the required python dictionary and store the result in a variable jsonData.
# Create an empty dictionary phoneRecord. This will store the result
# Loop over all names in the jsonData and store the names of the people and their phone numbers as key-value pairs in the phoneRecord dictionary.
# Use the json.dump() function to create a new json file which contains the phone records.