# String Checklist
# Create an empty string
empty_string = ""

# Determine if a string is empty
if not str_var:
    print("str_var is empty!")

if len(str_var) == 0:
    print("str_var is empty!")

# Format a string to contain dynamic data
name = "Fluffington"
str_var = f"Hello {name}"

# Access individual characters/items in a string
print(name[0])
print(name[-2])

# Access the first, access the last item in a string
print(name[0]) # first
print(name[len(name)-1]) # last
print(name[-1]) # last

# Join two/multiple strings together
a = "poo"
b = "poo"
c = a + b
print(c)

# Reverse a string
temp = park
reversed_temp = temp[::-1]
v2 = ''.join(reversed(temp))

# Create a copy of a string
temp = "hydroflask"
temp_copy = temp[:]
another_copy = temp

# Compare strings for equality
a = "marshall"
b = dog
status = a == b

# Determine the minimum and maximum value within a string
temp = "hydroflask"
print(max(temp))
print(min(temp))
print(max('hello', 'goodbye'))
print(min('1', '2', '3', '!'))

# Determine if an item or a pattern exists within a string
word = "poopooplatter"
if "poo" in word:
    print("yes")

# Locate the index of an item or a pattern exists within a string
poop_location = word.find("poo") # will not crash if doesn't exist
poop_location = word.index("poop")

# Count how often an item or a pattern occurs within a string
poop_count = word.count("poop")

# Convert all items in a string to uppercase/lowercase
yell_hydroflask = "hydroflask".upper() 
calm_hydroflask = yell_hydroflask.lower()

# Determine if the string can be converted to an integer
str_num = "67"
num = 0
if str_num.isdigit():
    num = int(str_num)

# Convert a string to an integer
num = int(str_num)

# Determine if a string only contains alphabetical characters
word  = "shsm".isalpha()

# Remove non-alphabetical characters from a string
gibberish = "!283y 40equi!@#$%Taisdka" 
clean = ""
i = 0
while i < len(gibberish):
    if gibberish[i].isalpha():
        clean += gibberish[i]
    i += 1

# Remove all alphabetical characters from a string
gibberish = "!283y 40equi!@#$%Taisdka" 
clean = ""
i = 0
while i < len(gibberish):
    # if not gibberish[i].isalpha()
    if gibberish[i].isalpha() == False:
        clean += gibberish[i]
    i += 1

# Remove all whitespaces from a string
example = " h h h h h h h h hh h h    e e ll o "
example = example.replace(" ", "")

# Sort a string in ASCII order or reverse-ASCII order


# Determine if a string follows a ruleset
