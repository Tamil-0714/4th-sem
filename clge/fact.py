# Aim 
    # To write a piton program to find factorila of an number using recursion

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

number = int(input("Enter the value to find the Factorial : "))
print(f"The factorial of {number} is:", factorial(number))



"""
Output :
    Enter the value to find the Factorial : 7
    The factorial of 7 is: 5040
"""