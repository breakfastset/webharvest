DATE_INDEX = 2
CLOSE_INDEX = 7

in_file = open("alibaba9988.txt", "r")

headers = in_file.readline()   # read first line and discard
for line in in_file:
    data = line.split(",")   # convert to a list
    current_date = data[DATE_INDEX]
    current_close = float(data[CLOSE_INDEX])
    print(current_date, current_close)

in_file.close()