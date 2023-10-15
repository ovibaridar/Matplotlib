import matplotlib.pyplot as plt

myfont = {
    'family': "Arial",
    'size': 20,
    'color': "green"
}
x = [1, 2, 3, 4]
x1 = [1, 2, 3, 4]
y = [0, 4, 9, 16]
y1 = [0, 1, 4, 5]

# Create the first subplot (1 row, 1 column, and select the first subplot)
plt.subplot(1, 2, 1)
# plt.subplot(2, 1, 1)
plt.title("MT", fontdict=myfont)
plt.xlabel("X-data")
plt.ylabel("y-data")
plt.grid(axis="y")
plt.plot(x, y, marker="h", ms=10, mfc="y", ls="dotted")

# Create the second subplot (1 row, 1 column, and select the second subplot)
plt.subplot(1, 2, 2)
# plt.subplot(2, 1, 2)
plt.title("MT2", fontdict=myfont)
plt.xlabel("X-data")
plt.ylabel("y-data")
plt.grid(axis="y")
plt.plot(x1, y1, marker="h", ms=10, mfc="y", ls="dotted")

plt.tight_layout()  # Optional, to improve subplot spacing

plt.show()
