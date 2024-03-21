


def is_prime(number):
    if number <= 1:
        return False
    elif number <= 3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

n = int(input('Enter an number to print prime numbers : '))
print(f"prime numbers form 1 to {n} are : ", end='')
for i in range(1, n+1):
    if is_prime(i):
        print(i,end=', ')


'''
output:
    Enter an number to print prime numbers : 15
    prime numbers form 1 to 15 are : 2, 3, 5, 7, 11, 13,
'''



