# for loop is used for fixed number of iterations.

for i in range(5): # for i in range(start=0, end=5, step=1):
    print(i)   # 0, 1, 2, 3, 4   [ does not include end ]

print("--" * 20)   # horizontal rule

for i in range(13, 20):  # start=13, end=20, step=1
    print(i)   # 13, 14, 15, 16, 17, 18, 19

print("--" * 20)   # horizontal rule
for i in range(10, 30, 5): # start=10, end=30, step=5
    print(i)   # 10, 15, 20, 25

print("--" * 20)   # horizontal rule
for char in "switzerland": # for x in collection
    print(char)

# collections are things like lists, sets, tuples, dictionaries
