# Aim 
    # To write a piton program to find fibonacci sequence of n number using recursion

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

num_terms = int(input('Enter the number of terms to print fibonacci sequence : '))
print("Fibonacci sequence:")
for i in range(num_terms):
    print(fibonacci(i), end=" ")


"""
Output:
    Enter the number of terms to print fibonacci sequence : 10
    Fibonacci sequence : 0 1 1 2 3 5 8 13 21 34

"""