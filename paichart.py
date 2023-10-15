import matplotlib.pyplot as plt

result_gread = ['F', 'D', 'C', 'B', 'A-', 'A', 'A+']
result_value = [10, 9, 20, 40, 50, 10, 5]
plt.pie(result_value, labels=result_gread, autopct='%2.2f%%', explode=[0.1, .1, 0.1, 0.1, .1, 0.1, 0.1])
plt.show()
