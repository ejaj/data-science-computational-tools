def read_file(file_name):
    graph = {}
    with open(file_name, 'r') as file:
        for line in file:
            parts = line.strip().split(':')
            vertex = parts[0].strip()
            neighbors = [neighbor.strip() for neighbor in parts[1].split(',')]
            graph[vertex] = neighbors
    return graph


# Step - 1: Map
def map_common_friends(graph):
    common_friends = {}
    # print(graph.items())
    for g_vertex, g_neighbors in graph.items():
        for g_vertex_1, g_neighbors_1 in graph.items():
            # print(g_vertex, g_vertex_1)
            if g_vertex != g_vertex_1:
                common_neighbors = set(g_neighbors).intersection(g_neighbors_1)
                # print(common_neighbors)
                if common_neighbors:
                    key = tuple(sorted([g_vertex, g_vertex_1]))
                    if key not in common_friends:
                        common_friends[key] = []
                    common_friends[key].extend(common_neighbors)
    return common_friends


# Step - 2: Reduce
def reduce_common_friends(common_friends):
    results = {}
    for key, common in common_friends.items():
        results[key] = list(set(common))
    return results


if __name__ == "__main__":
    filename = "../data/common-friends/friends.txt"
    g = read_file(filename)
    common_friends = map_common_friends(g)
    result = reduce_common_friends(common_friends)

    # Print the result in the desired format
    for key, common in result.items():
        vertex1, vertex2 = key
        print(f"{vertex1}, {vertex2} : {', '.join(common)}")
