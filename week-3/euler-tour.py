def read_graph_from_file(file_name):
    graph = {}
    with open(file_name, 'r') as file:
        for line in file:
            x, y = map(int, line.strip().split())
            # print(x, y)
            if x not in graph:
                graph[x] = []
            if y not in graph:
                graph[y] = []
            graph[x].append(y)
            graph[y].append(x)
    return graph


def count_even_and_odd_degrees(graph):
    even_count = odd_count = 0
    for vertex in graph:
        degree = len(graph[vertex])
        if degree % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count


def has_euler_tour(graph):
    even_count, odd_count = count_even_and_odd_degrees(graph)
    if even_count == len(graph):
        return True  # Euler circuit
    elif even_count == len(graph) - 2 and odd_count == 2:
        return True  # Euler path
    else:
        return False


if __name__ == "__main__":
    # filename = "../data/euler-graphs/eulerGraphs1.txt"
    filename = "../data/euler-graphs/eulerGraphs3.txt"
    graph = read_graph_from_file(file_name=filename)
    even_count, odd_count = count_even_and_odd_degrees(graph)
    # print(even_count, odd_count)
    if has_euler_tour(graph):
        print("The graph has an Euler tour.")
        print(f"Number of vertices with even degree: {even_count}")
        print(f"Number of vertices with odd degree: {odd_count}")
    else:
        print("The graph does not have an Euler tour.")
