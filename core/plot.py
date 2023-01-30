import matplotlib.pyplot as plt

# select the features to use for the x and y axis of the scatter plot
x = data["in_degree"]
y = data["out_degree"]

# get the cluster labels for each data point
labels = data["cluster"]

# create a scatter plot with different colors for each cluster
plt.scatter(x, y, c=labels)

# add labels and title
plt.xlabel("In-degree")
plt.ylabel("Out-degree")
plt.title("Scatter plot of clusters")

# show the plot
plt.show()
