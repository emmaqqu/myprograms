def perfect_num(val):
    divider = 1
    total = 0
    while divider < val:
        if val % divider == 0:
            total = total + divider
        divider += 1
    return total == val

number = int(input("Enter a number: "))
if perfect_num(number):
    print(f"{number} is a perfect number")
else:
    print(f"{number} is not a perfect number")