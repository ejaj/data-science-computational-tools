def find_triangles(graph):
    triangles = []
    for node1 in graph:
        for node2 in graph[node1]:
            for node3 in graph[node2]:
                if node3 != node1 and node3 in graph[node1]:
                    triangle = [node1, node2, node3]
                    triangle.sort()
                    if triangle not in triangles:
                        triangles.append(triangle)
    return triangles


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'E'],
    'E': ['C', 'D']
}

triangles = find_triangles(graph)
print("Triangles in the graph:")
for triangle in triangles:
    print(triangle)
