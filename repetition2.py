# while loop is meant for unknown number of repetitions
# 1. prime the loop
# while 2. condition is True:
#    3. statements
#    4. update var to make 2. eventually false
# 1 -> 2 -> 3 -> 4 -> 2 -> 3 -> 4 -> 2 (false) exit loop

count = 1        # prepare to enter loop
while count < 5:
    print(count)
    count = count + 1
print("Outside loop")