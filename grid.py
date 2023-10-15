import matplotlib.pyplot as plt

myfont = {

    'family': "Arial",
    'size': 20,
    'color': "green"
}
x = [1, 2, 3, 4]
y = [1, 4, 9, 16]

plt.title("MT", fontdict=myfont)
plt.xlabel("X-data")
plt.ylabel("y-data")
plt.plot(x, y, marker="h",ms=10, mfc="y", ls="dotted")
plt.grid(axis="both",ls="dashed",c="y",lw=1)
plt.show()
