from matplotlib import pyplot as plt

# sumbu x
movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]

# sumbu y
num_oscars = [5, 11, 3, 8, 10]

# bars are by default width 0.8, so we'll add 0.1 to the left coordinates
# so that each bar is centered 
xs = [i + 0.5 for i, _ in enumerate(movies)]

# plot bars with left x-coordinates [xs], heights [num_oscars]
plt.bar(xs, num_oscars)

# label x y dan judul
plt.ylabel("# of Academy Awards")
plt.xlabel('# Movie Names')

# judul
plt.title("My Favorite Movies")

# label x-axis with movie names at bar centers
# buat tataletak si label movies 
plt.xticks([i + 0.5 for i, _ in enumerate(movies)], movies)
plt.show()