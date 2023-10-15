import matplotlib.pyplot as plt

myfont = {

    'family': "Arial",
    'size': 20,
    'color': "green"
}
x = [1, 2, 3, 4]
y = [1, 4, 9, 16]
# Create Figure 1
plt.figure(1)
plt.plot(x, y, marker='h', c='b', mfc='b', mec='k', ms=20, lw=2)
plt.title('Figure 1', fontdict={'family': "Arial",
                                'size': 20,
                                'color': "black"})

# Create Figure 2
plt.figure(2)
plt.plot([1, 2, 3, 4], [1, 8, 27, 64], marker='.', c='y', mec='k', ms=20, lw=2)
plt.title('Figure 2', fontdict={'family': "Arial",
                                'size': 20,
                                'color': "red"})

plt.figure(3)
plt.plot([1, 2, 3, 4], [1, 8, 28, 64], marker='.', mfc='r', c='r', mec='k', ms=20, lw=2)
plt.title('Figure 3', fontdict=myfont)

plt.show()
