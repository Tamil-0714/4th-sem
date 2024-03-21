''' 
 Aim : to perform user defined and built in exception in python program 
'''

#Program 1 built in defined exception
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

#Program 2 user defined exception
class ValidMark(Exception):
    def __init__(self, message="Invalid mark. Please enter a valid mark."):
        self.message = message
        super().__init__(self.message)

marks = []
i = 0
while len(marks) < 5:
    try:
        mark = int(input(f"Enter Mark {i+1}: "))
        if mark < 0 or mark > 100:
            raise ValidMark()
        marks.append(mark)
        i += 1
    except ValidMark as er:
        print(er)

print("The marks are",marks)

'''
Output : 
    Enter Mark 1: 30
    Enter Mark 2: -2
    Invalid mark. Please enter a valid mark.
    Enter Mark 2: 40
    Enter Mark 3: 27
    Enter Mark 4: 109
    Invalid mark. Please enter a valid mark.
    Enter Mark 4: 111
    Invalid mark. Please enter a valid mark.
    Enter Mark 4: 84
    Enter Mark 5: 46
    The marks are [30, 40, 27, 84, 46]

'''


