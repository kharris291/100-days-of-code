print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

result = 0
if size == "S":
    result += 15
elif size == "M":
    result += 20
elif size == "L":
    result += 25
else:
    print("Please enter a valid size.")
    exit()

if pepperoni == "Y":
    if size == "S":
        result += 2
    else:
        result += 3

if extra_cheese == "Y":
    result += 1

print(f"Your final bill is: ${result}.")