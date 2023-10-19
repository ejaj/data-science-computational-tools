import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

X, y = load_iris(return_X_y=True)
print(X.shape)

# Elbow Method for value of k, Find optimum number of cluster
sse = []  # SUM OF SQUARED ERROR
for k in range(1, 11):
    km = KMeans(n_clusters=k, random_state=2)
    km.fit(X)
    sse.append(km.inertia_)

# Plot the Elbow graph to find the optimum number of cluster
sns.set_style("whitegrid")
g = sns.lineplot(x=range(1, 11), y=sse)
g.set(xlabel="Number of cluster (k)", ylabel="Sum Squared Error", title='Elbow Method')
plt.show()

# Silhouette Score Method for value of k, Find optimum number of cluster
silhouette_scores = []
for k in range(1, 11):
    km = KMeans(n_clusters=k, random_state=2)
    labels = km.fit_predict(X)
    if len(set(labels)) > 1:
        silhouette_avg = silhouette_score(X, labels)
        silhouette_scores.append(silhouette_avg)
    else:
        # If there's only one cluster, assign a Silhouette Score of -1
        silhouette_scores.append(-1)
print(silhouette_scores)
# Plot the Silhouette Score graph to find the optimum number of clusters
plt.plot(range(1, 11), silhouette_scores, marker='o')
plt.xlabel("Number of clusters (k)")
plt.ylabel("Silhouette Score")
plt.title("Silhouette Score Method")
plt.show()

"""
From the above graphs, we can observe that at k=2 and k=3 elbow-like situation. So, we are considering K=3
"""
kmeans = KMeans(n_clusters=3, random_state=2)
kmeans.fit(X)
print(kmeans.cluster_centers_)
pred = kmeans.fit_predict(X)
print(pred)

# Plot the cluster center with data points
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.scatter(X[:, 0], X[:, 1], c=pred, cmap=cm.Accent)
plt.grid(True)
for center in kmeans.cluster_centers_:
    center = center[:2]
    plt.scatter(center[0], center[1], marker='^', c='red')
plt.xlabel("petal length (cm)")
plt.ylabel("petal width (cm)")

plt.subplot(1, 2, 2)
plt.scatter(X[:, 2], X[:, 3], c=pred, cmap=cm.Accent)
plt.grid(True)
for center in kmeans.cluster_centers_:
    center = center[2:4]
    plt.scatter(center[0], center[1], marker='^', c='red')
plt.xlabel("sepal length (cm)")
plt.ylabel("sepal width (cm)")

plt.show()
