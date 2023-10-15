import matplotlib.pyplot as plt

myfont = {

    'family': "Arial",
    'size': 20,
    'color': "green"
}

# Create Figure 1
plt.figure(1)
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.title('Figure 1', fontdict={'family': "Arial",
                                'size': 20,
                                'color': "black"})

# Create Figure 2
plt.figure(2)
plt.plot([1, 2, 3, 4], [1, 8, 27, 64])
plt.title('Figure 2', fontdict={'family': "Arial",
                                'size': 20,
                                'color': "red"})

plt.figure(3)
plt.plot([1, 2, 3, 4], [1, 8, 28, 64])
plt.title('Figure 3', fontdict=myfont)

plt.show()  # Display both figures
