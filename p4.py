# Factors of a Number
import math
start = 1
num = int(input("Enter a number: "))
new_stop = int(math.sqrt(num)) + 1
factor_count = 0

while start < new_stop:
    if num % start == 0:
        dividend = num // start
        if start != dividend:
            factor_count += 2
            print(f"{start} and {dividend} are factors of {num}.")
        else:
            factor_count += 1
    start += 1
print(f"{num} has {factor_count} total factors.")