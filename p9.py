def fib(num):
    if num in {0, 1}:
        return num
    else: 
        location = 2
        two_before = 0
        one_before = 1
        total_sum = 0
        while location <= num:
            total_sum = two_before + one_before
            two_before = one_before
            one_before = total_sum
            location += 1

        return total_sum
# end of function

i = 0
while i < 10:
    print(f"N: {i} fib(N): {fib(i)}")
    i += 1