# Non-Destructive Selection Sort with Lists

# Selection Sort
def select(a_list):
    if len(a_list) <= 1:
        return a_list
    else:
        i = 0
        while i < len(a_list):
            smallest = a_list[i] # then prove it is or is not
            # start
            j = i + 1 # search from i + 1 onwards
            new_location = 1 # initialize
            while j < len(a_list):
                if a_list[j] < smallest: 
                    smallest = a_list[j]
                    new_location = j
                j += 1
            # end
            # swap smallest into proper location
            temporary = a_list[i]
            a_list[i] = smallest 
            a_list[new_location] = temporary
            # Python way
            # a_list[i], a_list[new_location] = a_list[new_location], a_list[i]
            i += 1

# Bubble Sort
def bubble(a_list):
    swapped = True
    while swapped: 
        swapped = False
        for i in range(1, len(a_list)):
            if a_list[i-1] > a_list[i]:
                swapped = True
                a_list[i-1], a_list[i] = a_list[i], a_list[i-1]
        # end of inner for
    # end of outer while
    return a_list

# Insertion Sort
def inserty(a_list):
    i = 1
    while i < len(a_list):
        j = i 
        while j > 0:
            if a_list[j-1] > a_list[j]:
                a_list[j-1], a_list[j] = a_list[j], a_list[j-1]
            else:
                break
            j -= 1
        i += 1
    return a_list

# CHALLENGE
def sort_it(a_list, b_list):
    pass

# Merge sort