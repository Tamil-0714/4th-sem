#program 1
import math
class Shape:
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height
class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2
# Usage
rectangle = Rectangle(5, 4)
print("Area of Rectangle:", rectangle.area()) # Output: 20
circle = Circle(3)
print("Area of Circle:", circle.area()) # Output: 28.274333882308138
triangle = Triangle(4, 3)
print("Area of Triangle:", triangle.area()) # Output: 6.0
square = Square(5)
print("Area of Square:", square.area()) 

#--------------------------------------------------------------------------------------------------------------#

# program 2


# Aim
    # To write a piton program to implement class concepts with simple students details

class Student:
    def __init__(self, data):
        self.name = data['Name']
        self.id = data['Id']
        self.age = data['Age']
        self.cgpa = data['cgpa']
        self.phone = data['Phone']

    def display_info(self):
        print("Name         : ", self.name)
        print("Register No. : ", self.id)
        print("Age          : ", self.age)
        print("CGPA         : ", self.cgpa)
        print("Contact No.  : ", self.phone)
    
    def update_std_detaild(self,prototype, value):
        setattr(self, prototype, value)

std_data = [
    {
    'Name' : "Tamil",
    'Id' : "22UCS626",
    'Age' : 19,
    'cgpa' : 77.77,
    'Phone' : "+91 99431 12938",
    },
    {
    'Name' : "June",
    'Id' : "22UCS625",
    'Age' : 17,
    'cgpa' : 83.72,
    'Phone' : "+91 81483 94597",
    },

]

# Creating an instance of the Student class
student1 = Student(std_data[0])
student2 = Student(std_data[1])

# Accessing student 1
student1.display_info()
student1.update_std_detaild('name',"Tamilarasan N")
student1.update_std_detaild('cgpa',67.19)
student1.display_info()

# Accessing student 2
student2.display_info()
student2.update_std_detaild('cgpa',85.72)
student2.display_info()

"""
Output : 

    Name         :  Tamil
    Register No. :  22UCS626
    Age          :  19
    CGPA         :  77.77
    Contact No.  :  +91 99431 12938

    Name         :  Tamilarasan N
    Register No. :  22UCS626
    Age          :  19
    CGPA         :  67.19
    Contact No.  :  +91 99431 12938

    Name         :  June
    Register No. :  22UCS625
    Age          :  17
    CGPA         :  83.72
    Contact No.  :  +91 81483 94597

    Name         :  June
    Register No. :  22UCS625
    Age          :  17
    CGPA         :  85.72
    Contact No.  :  +91 81483 94597


"""

#--------------------------------------------------------------------------------------------------------------#

 # program 4

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")
class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors
    def display_info(self):
        super().display_info()
        print(f"Number of doors: {self.num_doors}")
class Motorcycle(Vehicle):
    def __init__(self, make, model, year, engine_size):
        super().__init__(make, model, year)
        self.engine_size = engine_size
    def display_info(self):
        super().display_info()
        print(f"Engine size: {self.engine_size} cc")
# Usage
car = Car("Toyota", "Camry", 2022, 4)
car.display_info()
print()
motorcycle = Motorcycle("Harley-Davidson", "Sportster", 2020, 1200)
motorcycle.display_info()


#--------------------------------------------------------------------------------------------------------------#

# program 5


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Scholar:
    def __init__(self, scholarship_amount):
        self.scholarship_amount = scholarship_amount

    def display_scholarship_info(self):
        print(f"Scholarship Amount: ${self.scholarship_amount}")

class Student(Person, Scholar):
    def __init__(self, name, age, scholarship_amount, grade):
        Person.__init__(self, name, age)
        Scholar.__init__(self, scholarship_amount)
        self.grade = grade

    def display_info(self):
        super().display_info()
        super().display_scholarship_info()
        print(f"Grade: {self.grade}")
        
person = Person("Ravi",25)
print("Normal person : ")
person.display_info()
student = Student("Tamil", 19, 29000, "A")
print("Student : ")
student.display_info()


'''
output :
    Normal person : 
        Name: Ravi, Age: 25

    Student : 
        Name: Tamil, Age: 19
        Scholarship Amount: $29000
        Grade: A

'''


#program 6 
#--------------------------------------------------------------------------------------------------------------#

''' 
 Aim : to perform user defined exception in python program
'''

try:
    a=int(input("First Number:"))
    b=int(input("Second Number:")) 
    result=a/b
    print(result)
except ZeroDivisionError: 
    print("Division by Zero")
else:
    print("Successful Division")
          
'''
output : 
    First Number:10
    Second Number:0
    Division by Zero

    First Number:10
    Second Number:2
    5.0
    Successful Division

'''


#program 7
#--------------------------------------------------------------------------------------------------------------#

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

#program 8
#--------------------------------------------------------------------------------------------------------------#

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




