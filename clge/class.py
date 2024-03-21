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