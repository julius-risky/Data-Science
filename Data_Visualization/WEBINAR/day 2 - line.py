# import library matplotlib -> untuk plotting
# pyplot -> didalam matplotlib itu ada module? namanya pyplot yang diinisalin plt
from matplotlib import pyplot as plt

# ada 3 line
variance = [1, 2, 4, 8, 16, 32, 64, 128, 256, 100]
bias_squared = [2, 128, 64, 32, 16, 8, 4, 2, 1, 1]
total_error = [x + y for x, y in zip(variance, bias_squared)]

# biar letaknya ditengah
xs = [i for i, _ in enumerate(variance)]

# we can make multiple calls to plt.plot
# to show multiple series on the same chart
plt.plot(xs, variance, 'g-', label='variance') # green solid line
plt.plot(xs, bias_squared, 'r^', label='bias^2') # red dot-dashed line
plt.plot(xs, total_error, 'b:', label='total error') # blue dotted line

# because we've assigned labels to each series
# we can get a legend for free
# loc=9 means "top center"
plt.legend(loc="best")
plt.xlabel("model complexity")
plt.title("The Bias-Variance Tradeoff")
plt.show()