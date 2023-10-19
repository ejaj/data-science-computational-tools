import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

X, y = make_blobs(n_samples=500, n_features=2, centers=3, random_state=23)
fig = plt.figure(0)
plt.grid(True)
plt.scatter(X[:, 0], X[:, 1])
plt.show()

# initialize the random centroids
k = 3
clusters = {}
np.random.seed(32)
for idx in range(k):
    center = 2 * (2 * np.random.random((X.shape[1],)) - 1)
    points = []
    cluster = {
        'center': center,
        'points': []
    }
    clusters[idx] = cluster
print(clusters)


# print(clusters)

# Plot the random initialize center with data points
plt.scatter(X[:, 0], X[:, 1])
plt.grid(True)
for i in clusters:
    center = clusters[i]['center']
    plt.scatter(center[0], center[1], marker='*', c='red')
plt.show()


# euclidean distance
def distance(p1, p2):
    # print("dis",np.sqrt(np.sum((p1 - p2) ** 2)) )
    return np.sqrt(np.sum((p1 - p2) ** 2))


# Implementing euclidean step
def assign_clusters(X, clusters):
    for idx in range(X.shape[0]):
        dist = []
        current_x = X[idx]
        for i in range(k):
            # print(clusters[i])
            dis = distance(current_x, clusters[i]['center'])
            dist.append(dis)
        curr_cluster = np.argmin(dist)
        clusters[curr_cluster]['points'].append(current_x)
    return clusters


# Implementing the Mean Step
def update_clusters(X, clusters):
    for i in range(k):
        points = np.array(clusters[i]['points'])
        if points.shape[0] > 0:
            new_center = points.mean(axis=0)
            clusters[i]['center'] = new_center

            clusters[i]['points'] = []
    return clusters


# Predict the cluster for the datapoints
def pred_cluster(X, clusters):
    pred = []
    for i in range(X.shape[0]):
        dist = []
        for j in range(k):
            dist.append(distance(X[i], clusters[j]['center']))
        pred.append(np.argmin(dist))
    return pred


clusters = assign_clusters(X, clusters)
clusters = update_clusters(X, clusters)
pred = pred_cluster(X, clusters)

# Plot the data points with their predicted cluster center
plt.scatter(X[:, 0], X[:, 1], c=pred)
for i in clusters:
    center = clusters[i]['center']
    plt.scatter(center[0], center[1], marker='^', c='red')
plt.show()
