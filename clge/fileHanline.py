# Aim :
    # To perfrom file handling operation on python such as creation a file , reading, writting, editing a text file  

def create_file(file_name):
    with open(file_name, 'w') as file:
        file.write("Hello, this is a sample text file!\n")
        file.write("We can perform read and write operations on this file.")
    print(f"File '{file_name}' created successfully.")

def read_file(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
    print(f"Content of file '{file_name}':\n{content}")

def write_file(file_name, new_content):
    with open(file_name, 'a') as file:
        file.write("\n" + new_content)
    print("Content appended to file successfully.")

file_name = "sample.txt"

create_file(file_name)

read_file(file_name)

new_content = "This is new content appended to the file."
write_file(file_name, new_content)

read_file(file_name)



'''
output :
 
    File 'sample.txt' created successfully.
    Content of file 'sample.txt':
    Hello, this is a sample text file!
    We can perform read and write operations on this file.
    Content appended to file successfully.
    Content of file 'sample.txt':
    Hello, this is a sample text file!
    We can perform read and write operations on this file.
    This is new content appended to the file.

'''