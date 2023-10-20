import numpy as np

# Sample data
data = np.array([
    [1, 2],
    [1, 4],
    [1, 0],
    [4, 2],
    [4, 4],
    [4, 0]
])

# Step 1: Random Sampling
sample_indices = np.random.choice(len(data), size=2, replace=False)
sample = data[sample_indices]
# print(sample)

# Step 2: Hierarchical Clustering
# In a simple example, we'll manually calculate distances and form clusters.

clusters = [{i} for i in range(len(sample))]  # Initialize each data point as a cluster

while len(clusters) > 2:
    min_distance = float('inf')
    merge_clusters = None

    for i in range(len(clusters)):
        for j in range(i + 1, len(clusters)):
            # Calculate distance between clusters (e.g., using Euclidean distance)
            cluster_i = np.mean(sample[list(clusters[i]), :], axis=0)
            cluster_j = np.mean(sample[list(clusters[j]), :], axis=0)
            distance = np.linalg.norm(cluster_i - cluster_j)

            if distance < min_distance:
                min_distance = distance
                merge_clusters = (i, j)

    i, j = merge_clusters
    clusters[i].update(clusters[j])  # Merge the clusters
    clusters.pop(j)
# Step 4: Reduce Representatives
representatives = [np.mean(sample[list(cluster), :], axis=0) for cluster in clusters]
# Step 6: Assign Data Points
cluster_assignments = []
for data_point in data:
    closest_representative_index = -1
    min_distance = float('inf')

    for idx, representative in enumerate(representatives):
        distance = np.linalg.norm(data_point - representative)
        if distance < min_distance:
            min_distance = distance
            closest_representative_index = idx

    cluster_assignments.append(closest_representative_index)


# Print the cluster assignments
for i, assignment in enumerate(cluster_assignments):
    print(f"Data point {i} is assigned to Cluster {assignment}")

# Initialize a variable to store the Davies-Bouldin Index
davies_bouldin_index = 0.0

# Calculate Davies-Bouldin Index
for i in range(len(clusters)):
    max_diameter = 0  # Initialize the maximum diameter for cluster i

    # Calculate the average distance between the data points and the centroid of cluster i
    for j in range(len(clusters)):
        if i != j:
            # Calculate the Euclidean distance between the centroids of clusters i and j
            distance_ij = np.linalg.norm(representatives[i] - representatives[j])

            # Calculate the average distance from data points in cluster i to its centroid
            avg_distance_i = np.mean([np.linalg.norm(data[p] - representatives[i]) for p in clusters[i]])
            avg_distance_j = np.mean([np.linalg.norm(data[q] - representatives[j]) for q in clusters[j]])

            # Calculate the Davies-Bouldin index for cluster i and cluster j
            db_index = (avg_distance_i + avg_distance_j) / distance_ij

            if db_index > max_diameter:
                max_diameter = db_index

    davies_bouldin_index += max_diameter

# Divide by the number of clusters to get the average Davies-Bouldin Index
davies_bouldin_index /= len(clusters)

# Print the Davies-Bouldin Index
print(f"Davies-Bouldin Index: {davies_bouldin_index}")


