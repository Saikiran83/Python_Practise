
def modify_string(original):
    original += " that has been modified"
    print(original)
def modify_string_return(original):
    original += " that has been return "
    return original

test_string = "This is a test string"
b = modify_string(test_string)
# print(b)
a = modify_string_return(test_string)
print(a)