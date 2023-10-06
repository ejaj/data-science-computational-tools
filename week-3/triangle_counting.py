def read_graph(filename):
    graph = {}
    with open(filename, 'r') as file:
        for line in file:
            vertex1, vertex2 = map(int, line.strip().split())
            if vertex1 not in graph:
                graph[vertex1] = set()
            if vertex2 not in graph:
                graph[vertex2] = set()
            graph[vertex1].add(vertex2)
            graph[vertex2].add(vertex1)
    return graph


def map_triangles(graph):
    triangles = 0
    for vertex1 in graph:
        for vertex2 in graph[vertex1]:
            if vertex1 < vertex2:
                neighbors1 = graph[vertex1]
                neighbors2 = graph[vertex2]
                common = neighbors1.intersection(neighbors2)
                for vertex3 in common:
                    if vertex1 < vertex3 < vertex2:
                        triangles += 1

    return triangles


if __name__ == "__main__":
    filename = "../data/roadnet/roadnet.txt"
    g = read_graph(filename)
    triangle_count = map_triangles(g)
    print(f"Number of triangles in the graph: {triangle_count}")
