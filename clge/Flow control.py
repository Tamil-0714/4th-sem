marks = []
result = True
for i in range(5):
    mark = float(input(f"Enter mark {i+1}: "))
    marks.append(mark)

average = sum(marks) / len(marks)
for mark in marks:
    if mark < 35 :
        result = False
if result:  
    print("Congratulations! The student has passed.")
    if average >= 90:
        grade = 'A'
    elif average >= 80:
        grade = 'B'
    elif average >= 70:
        grade = 'C'
    elif average >= 60:
        grade = 'D'
    else:
        grade = 'F'
    print(f"Total: {sum(marks)}")
    print(f"Average: {average}")
    print(f"Grade: {grade}")
else:
    print("Sorry, the student has failed.")

'''
output:
    Enter mark 1: 45
    Enter mark 2: 55
    Enter mark 3: 65
    Enter mark 4: 89
    Enter mark 5: 90
    Congratulations! The student has passed.
    Total: 344.0
    Average: 68.8
    Grade: D

'''