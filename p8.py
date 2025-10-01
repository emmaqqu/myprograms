# Prime Number Checker
import math

def is_prime(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    else: 
        divider = 3
        upper_limit = math.sqrt(num) + 1
        while divider < max(upper_limit, 3):
            if num % divider == 0:
                return False
            divider += 2
        return True

num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is a prime number ")
else:
    print(f"{num} is not a prime number")

# def prime_num(val):
#     divider = 1
#     counter = 0

#     while num >= divider:
#         if num % divider == 0:
#             counter += 1
#         divider += 1

#     if counter <= 2:
#         return True
        
# num = int(input("Enter a number: "))
# if prime_num(num):
#     print(f"{num} is a prime number ")
# else:
#     print(f"{num} is not a prime number")
