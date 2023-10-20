# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.cluster.hierarchy import dendrogram, linkage
# from scipy.spatial.distance import pdist
#
# # Sample data points (2D)
# data = np.array([[1, 2], [2, 3], [2, 4], [3, 2], [6, 7], [7, 8], [8, 7], [9, 8]])
#
# # Calculate the pairwise distances between data points
# distances = pdist(data)
#
# # Perform hierarchical clustering (using the 'ward' method)
# linkage_matrix = linkage(distances, method='ward')
#
# # Create and display a dendrogram
# dendrogram(linkage_matrix)
#
# plt.title('Hierarchical Clustering Dendrogram')
# plt.show()


import numpy as np

# Sample data points (2D)
data = np.array([[1, 2], [2, 3], [2, 4], [3, 2], [6, 7], [7, 8], [8, 7], [9, 8]])

# Initialize each data point as a cluster
clusters = [{"points": [point]} for point in data]


# Function to calculate the Euclidean distance between two points
def euclidean_distance(point1, point2):
    return np.sqrt(np.sum((point1 - point2) ** 2))


# Function to find the closest pair of clusters
def find_closest_clusters():
    min_distance = float("inf")
    closest_clusters = (0, 1)

    for i in range(len(clusters)):
        for j in range(i + 1, len(clusters)):
            distance = euclidean_distance(clusters[i]["points"][0], clusters[j]["points"][0])
            if distance < min_distance:
                min_distance = distance
                closest_clusters = (i, j)

    return closest_clusters


# Hierarchical clustering (single-linkage)
cluster_history = [{"clusters": [dict(c) for c in clusters]}]

while len(clusters) > 1:
    i, j = find_closest_clusters()
    clusters[i]["points"].extend(clusters[j]["points"])
    del clusters[j]

    cluster_history.append({"clusters": [dict(c) for c in clusters]})


# Display the hierarchical structure
def display_hierarchy(history):
    for level, data in enumerate(history):
        print(f"Level {level}:")
        for i, cluster in enumerate(data["clusters"]):
            print(f"  Cluster {i}: {len(cluster['points'])} points")


display_hierarchy(cluster_history)
