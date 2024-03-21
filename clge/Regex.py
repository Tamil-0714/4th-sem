# Aim :
    # To write a python program to perform Regular expression operations on python such as search() match() replace-> sub(), findall()


# program 1:
import re

# Sample text
text = "The cat sat on the mat."

pattern = r'cat'

match_result = re.match(pattern, text)
if match_result:
    print("Match found with match():", match_result.group())
else:
    print("No match found with match()")

search_result = re.search(pattern, text)
if search_result:
    print("Match found with search():", search_result.group())
else:
    print("No match found with search()")

'''

output : 
    No match found with match()
    Match found with search(): cat
'''


#Program 2
import re

text = "Hilo, my name is Tamil. You can reach me at tamil.tj.1967@gmail.com"
email_pattern = r'([\w\.-]+)@([\w\.-]+)' # email validation pattern

matches = re.findall(email_pattern, text)
print("Email addresses found:")
for match in matches:
    print(f"Username: {match[0]}, Mail-Domain: {match[1]}")

replaced_text = re.sub(email_pattern, r'<22ucs626@mail.sjctni.edu>', text) # replasing the exisisting email
print("\nNew replaced Email : ")
print(replaced_text)

'''
output : 

    Email addresses found:
    Username: tamil.tj.1967, Mail-Domain: gmail.com

    New replaced Email : 
    Hello, my name is Tamil. You can reach me at <22ucs626@mail.sjctni.edu>

'''

