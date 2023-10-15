import matplotlib.pyplot as plt

myfont = {

    'family': "Arial",
    'size': 20,
    'color': "green"
}
x = [1, 2, 3, 4]
y = [1, 4, 9, 16]
y2 = [0, 3, 5, 8]

plt.title("MT", fontdict=myfont)
plt.xlabel("X-data")
plt.ylabel("y-data")
plt.scatter(x, y, marker="h", c="r", label="sell in Sunday",lw=5)
plt.scatter(x, y2, c="b", label="sell in Monday",lw=5)
plt.legend()
plt.show()
