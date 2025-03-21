print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    if height <= 140:
        print("You can ride the rollercoaster")
    else:
        print("You're too tall and can't ride the rollercoaster")
else:
    print("Sorry you have to grow taller before you can ride.")
