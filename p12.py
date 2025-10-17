# Product Codes CCC '25 J3
def cleaner(text):
    uppercase = ""
    positives = ""
    negatives = ""
    total_sum = 0

    for item in text:
        if item.isalpha() and item.isupper():
            uppercase += item
            if len(positives) > 0: 
                total_sum += int(positives)
                positives = ""
            if len(negatives) > 0:
                total_sum += int(negatives)
                negatives = ""
        elif item == "-":
            if len(negatives) > 0:
                total_sum += int(negatives)
                negatives = ""
            else:
                negatives = "-"
        elif item.isdigit():
            if len(negatives) > 0:
                negatives += item
            else:
                positives += item
    # end of for loop

    if len(positives) > 0: 
        total_sum += int(positives)
    if len(negatives) > 0:
        total_sum += int(negatives)

    product_code = uppercase + str(total_sum)
    return product_code
# end of function

n = int(input("How many product codes need to be updated?" ))
for x in range(n):
    code = input("Enter product code: ")
    print(cleaner(code))