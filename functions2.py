# define a function called "can_vote"
# taking in 2 parameters "citizenship" and "age"
def can_vote(citizenship, age):
    if citizenship == "sg" and age >= 21:
        return True
    else:
        return False

print(can_vote("sg", 25))  # True
print(can_vote("sg", 20))  # False
print(can_vote("pr", 28))  # False