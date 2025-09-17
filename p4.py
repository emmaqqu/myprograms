# Factors of a Number
start = 1
end = int(input("Enter a number: "))
factor_count = 0

while start <= end:
    result = end / start
    if end % start == 0:
        print(f"{end} has a factor of {start}")
        factor_count +=1
    start += 1
print(f"{end} has {factor_count} total factors")
if factor_count == 2:
    print(f"{end} is a prime number.")
else:
    print(f"{end} is a composite number.")