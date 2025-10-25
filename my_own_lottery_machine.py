import random

MINIMUM_NUMBER = 1           # constants
MAXIMUM_NUMBER = 40
LOTTERY_NUMBERS_COUNT = 5

numbers = []    # an empty list.
while len(numbers) < LOTTERY_NUMBERS_COUNT:
    current_number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
    # get a random number from 1 to 40
    if current_number not in numbers:    # if not found
        numbers.append(current_number)   #     then add to the list

print("The numbers generated are:")
print(sorted(numbers))
