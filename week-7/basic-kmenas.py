import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
X = np.array([[1, 2], [5, 8], [1.5, 1.8], [8, 8], [1, 0.6], [9, 11]])

# Number of clusters
K = 2
# Initialize cluster centers randomly
np.random.seed(0)
# print(np.random.choice(X.shape[0], K, replace=False))
centers = X[np.random.choice(X.shape[0], K, replace=False)]
print(centers)
# Maximum number of iterations
max_iters = 100
for _ in range(max_iters):
    # Assign each data point to the nearest cluster center
    labels = np.argmin(np.linalg.norm(X[:, np.newaxis] - centers, axis=2), axis=1)
    # print(labels)
    # Update cluster centers as the mean of points in each cluster
    new_centers = np.array([X[labels == k].mean(axis=0) for k in range(K)])
    if np.all(centers == new_centers):
        break

    centers = new_centers
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
plt.scatter(centers[:, 0], centers[:, 1], marker='x', s=200, c='red')
plt.title("K-Means Clustering")
plt.show()
