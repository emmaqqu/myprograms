# Donut shop
# 09/16/2025

donuts = int(input("Enter # of donuts: "))
num_events = int(input("Enter # of events: "))
current_event = 1

while current_event <= num_events and donuts >= 0:
    events = input("Did you bake + or sell - donuts? ")
    q = int(input("How many donuts did you bake/sell? "))
    if events == "+":
        donuts = donuts + q
    elif events == "-":
        donuts = donuts - q
    current_event = current_event + 1

print(f"There is {donuts} donuts left")