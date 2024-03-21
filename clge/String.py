
sample_string = "Hello, World! This is a sample string for Python string methods."
print("capitalize():", sample_string.capitalize())
print("upper():", sample_string.upper())
print("lower():", sample_string.lower())
print("title():", sample_string.title())
print("swapcase():", sample_string.swapcase())
print("count('is'):", sample_string.count('is'))
print("find('World'):", sample_string.find('World'))
print("replace('Hello', 'Hi'):", sample_string.replace('Hello', 'Hi'))
print("split(' '):", sample_string.split(' '))
print("strip():", sample_string.strip())
print("isalpha():", sample_string.isalpha())
print("isnumeric():", sample_string.isnumeric())
print("isalnum():", sample_string.isalnum())
print("startswith('Hello'):", sample_string.startswith('Hello'))
print("endswith('methods.'):", sample_string.endswith('methods.'))

'''
output: 
    capitalize(): Hello, world! this is a sample string for python string methods.
    upper(): HELLO, WORLD! THIS IS A SAMPLE STRING FOR PYTHON STRING METHODS.
    lower(): hello, world! this is a sample string for python string methods.
    title(): Hello, World! This Is A Sample String For Python String Methods.
    swapcase(): hELLO, wORLD! tHIS IS A SAMPLE STRING FOR pYTHON STRING METHODS.
    count('is'): 2
    find('World'): 7
    replace('Hello', 'Hi'): Hi, World! This is a sample string for Python string methods.
    split(' '): ['Hello,', 'World!', 'This', 'is', 'a', 'sample', 'string', 'for', 'Python', 'string', 'methods.']
    strip(): Hello, World! This is a sample string for Python string methods.
    isalpha(): False
    isnumeric(): False
    isalnum(): False
    startswith('Hello'): True
    endswith('methods.'): True

'''



