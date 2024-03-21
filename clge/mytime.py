# import re
# text = "The cat sat on the mat"

# pattern = r'cat'

# match_result = re.match(pattern,text)
# if match_result :
#     print("mathc found",match_result.group())
# else :
#     print("match not fould")

# search_result = re.search(pattern,text)
# if search_result:
#     print("result fould ",search_result.group())
# else :
#     print("result  not foudn")




# def creatingFile(file_name):
#     with open(file_name,'w') as file:
#         file.write("some nwe content")
#         file.write("second line content")
#     print(f"FIle {file_name} has been created successfully")

# def readFile(file_name):
#     with open(file_name,'r') as file:
#         content = file.read()
#     print(content)

# def writeFile(file_name,new_content):
#     with open(file_name,'a') as file:
#         file.write("\n"+new_content)
#     print("content appended successfuly")

# fileName = "new.txt"
# creatingFile(fileName)
# readFile(fileName)
# writeFile(fileName, "THis is the new content added after ")
# readFile(fileName)


try:
    a = int(input("filest : "))
    b = int(input("second : "))
    res = a/b
    print(res)
except ZeroDivisionError:
    print("cant divide by zero")

else:
    print("division successfully")


