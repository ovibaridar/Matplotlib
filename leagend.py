import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7]
y1 = [0, 3, 6, 7, 2, 8, 8]
y2 = [0, 1, 3, 5, 2, 7, 5]
plt.xlabel("X-Data")
plt.ylabel("Y-Data")
plt.plot(x, y1, label="Sell in June", marker='h')  # Fixed the typo here
plt.plot(x, y2, label="Sell in July", marker='o')  # Fixed the typo here
plt.legend(loc="upper center", facecolor="w", edgecolor="k", framealpha=0.5, shadow=False, fancybox=True)
plt.grid(axis="y")
plt.show()
