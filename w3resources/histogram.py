import matplotlib.pyplot as plt

#create list of data
x = [2, 4, 4, 5, 6, 6, 7, 7, 7, 8, 8, 8, 12, 13]

#create histogram with 4 bins
plt.hist(x, bins=4, edgecolor='black')
plt.show()