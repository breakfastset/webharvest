import matplotlib.pyplot as plt
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

def plot_chart(x, y, title, x_label, y_label):
    plt.plot(x, y)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()

def main():
    # read data from file to get x and y data
    filename = "alibaba9988.txt"
    x, y = read_data(filename, DATE_INDEX, CLOSE_INDEX)

    lowest_price = min(y)
    highest_price = max(y)

    title_value = f"Alibaba: {lowest_price} - {highest_price}"

    # pass x and y to plot_chart() to plot
    plot_chart(x, y, title_value, "Date", "Close")

main()