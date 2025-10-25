import matplotlib.pyplot as plt

x = [2, 3, 4, 8, 9]
y = [5, 8, 10, 20, 15]

plt.plot(x, y)
plt.title("Savings over time")
plt.xlabel("Time (day)")
plt.ylabel("Savings ($)")
plt.show()     # display the chart