import matplotlib.pyplot as plt

x = [2010, 2013, 2016, 2019, 2022]
y = [8000, 18000, 22000, 30000, 45000]

plt.xlabel("Years")
plt.ylabel("sell")
plt.title("Fruity sell in every year")
plt.bar(x, y)
plt.plot(x, y, marker="o", ms=10, mfc='r', ls="none")
plt.show()
