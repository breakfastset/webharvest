DATE_INDEX = 2
CLOSE_INDEX = 7

def read_data(filename, x_index, y_index):
    x = []
    y = []
    in_file = open(filename, "r")
    headers = in_file.readline()   # read first line and discard
    for line in in_file:
        data = line.split(",")   # convert to a list
        current_date = data[x_index]
        current_close = float(data[y_index])
        x.append(current_date)
        y.append(current_close)
    in_file.close()
    return x, y

x_data, y_data = read_data("alibaba9988.txt", DATE_INDEX, CLOSE_INDEX)
print(x_data)
print(y_data)