import random

# Sample data points (2D)
data = [(1, 2), (5, 8), (1.5, 1.8), (8, 8), (1, 0.6), (9, 11)]

# Number of clusters (you can change this to experiment)
num_clusters = 2

# Define the number of iterations for the K-Means algorithm
num_iterations = 4

# Randomly initialize cluster centers
cluster_centers = [data[i] for i in range(num_clusters)]


# print(cluster_centers)


# Function to assign data points to the nearest cluster
def assign_to_clusters(data, centers):
    clusters = [[] for _ in range(len(centers))]
    for point in data:
        distances = [((point[0] - center[0]) ** 2 + (point[1] - center[1]) ** 2) ** 0.5 for center in centers]
        # print(distances)
        nearest_cluster = distances.index(min(distances))
        # print(nearest_cluster)
        clusters[nearest_cluster].append(point)
    # print(clusters)
    return clusters


# Function to update cluster centers
def update_centers(clusters):
    # new_centers = [
    #     (sum(point[0] for point in cluster) / len(cluster), sum(point[1] for point in cluster) / len(cluster)) for
    #     cluster in clusters
    # ]
    new_centers = []
    for cluster in clusters:
        sum_x = 0
        sum_y = 0
        num_points = len(cluster)
        for point in cluster:
            sum_x += point[0]
            sum_y += point[1]
        new_center_x = sum_x / num_points
        new_center_y = sum_y / num_points
        new_centers.append((new_center_x, new_center_y))
    # print(new_centers)
    return new_centers


# K-Means clustering
for _ in range(num_iterations):
    clusters = assign_to_clusters(data, cluster_centers)
    new_centers = update_centers(clusters)
    # Check for convergence
    if new_centers == cluster_centers:
        break

    cluster_centers = new_centers

# Print cluster assignments
for i, cluster in enumerate(clusters):
    print(f"Cluster {i + 1}: {cluster}")

# Print cluster centers
print("Cluster Centers:")
for i, center in enumerate(cluster_centers):
    print(f"Cluster {i + 1}: {center}")
