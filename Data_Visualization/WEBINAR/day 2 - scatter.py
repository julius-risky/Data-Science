from matplotlib import pyplot as plt
import scipy as sc
import numpy as np
friends = [ 7, 6, 2, 3, 1, 4, 6, 4, 7]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

# scatter plot
plt.scatter(friends, minutes)

# label each point
for label, friend_count, minute_count in zip(labels, friends, minutes):
    plt.annotate(label,
        xy=(friend_count, minute_count), # put the label with its point
        xytext=(5, -5), # but slightly offset
        textcoords='offset points')
corelasi =np.core(friends,minutes)
print(corelasi)
plt.title("Daily Minutes vs. Number of Friends")
plt.xlabel("# of friends")
plt.ylabel("daily minutes spent on the site")
plt.show()