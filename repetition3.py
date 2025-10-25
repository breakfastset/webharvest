count = 0
number = int(input("Enter a number (-ve to exit): ")) # 1. prime loop

while number >= 0:   # number is positive 2. while condition
    print(number)        # 3. statement 1
    count = count + 1    #    statement 2
    number = int(input("Enter a number (-ve to exit): ")) # 4. update
print(f"You entered {count} positive numbers.")