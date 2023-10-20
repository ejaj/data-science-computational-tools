import numpy as np


def distance(point1, point2):
    return np.linalg.norm(point1 - point2)


def get_neighbors(data, point, eps):
    neighbors = []
    for i in range(len(data)):
        if distance(data[i], point) <= eps:
            neighbors.append(i)
    return neighbors


def dbscan(data, eps, min_samples):
    n = len(data)
    labels = [0] * n  # Initialize all points as unvisited (0)

    cluster_id = 0

    for i in range(n):
        if labels[i] != 0:  # Skip visited points
            continue

        neighbors = get_neighbors(data, data[i], eps)

        if len(neighbors) < min_samples:
            labels[i] = -1  # Mark as noise/outlier
        else:
            cluster_id += 1
            expand_cluster(data, labels, i, neighbors, cluster_id, eps, min_samples)

    return labels


def expand_cluster(data, labels, point_index, neighbors, cluster_id, eps, min_samples):
    labels[point_index] = cluster_id

    i = 0
    while i < len(neighbors):
        neighbor_index = neighbors[i]

        if labels[neighbor_index] == -1:
            labels[neighbor_index] = cluster_id
        elif labels[neighbor_index] == 0:
            labels[neighbor_index] = cluster_id

            new_neighbors = get_neighbors(data, data[neighbor_index], eps)
            if len(new_neighbors) >= min_samples:
                neighbors += new_neighbors

        i += 1


# Sample data
data = np.array([[1, 2], [2, 2], [2, 3], [8, 7], [8, 8], [9, 7], [20, 20]])

# Parameters
eps = 2.0
min_samples = 2

# Perform DBSCAN clustering
labels = dbscan(data, eps, min_samples)

# Print the cluster assignments
for i in range(len(data)):
    if labels[i] == -1:
        print(f"Point {i}: Noise")
    else:
        print(f"Point {i}: Cluster {labels[i]}")
