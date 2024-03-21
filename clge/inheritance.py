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