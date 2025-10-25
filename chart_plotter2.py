import matplotlib.pyplot as plt

def plot_chart(x, y, title, x_label, y_label):
    plt.plot(x, y)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()

x = [1, 2, 3]
y = [4, 5, 6]
plot_chart(x, y, "test title", "x", "y")