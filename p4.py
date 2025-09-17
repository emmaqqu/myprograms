# Factors of a Number
start = 1
end = int(input("Enter a number: "))

while start <= end:
    result = end / start
    if end % start == 0:
        print(start)
    start += 1