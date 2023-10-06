from collections import defaultdict

# Adjacency list representation of tree
adj = defaultdict(list)

# Visited dictionary to keep track of visited nodes on our tour
visited = defaultdict(bool)

MAX = 1001
euler = [0] * (2 * MAX)


def add_edge(u, v):
    adj[u].append(v)
    adj[v].append(u)
    # print(adj[u])


def euler_tree(u, index):
    visited[u] = True
    euler[index] = u
    index += 1
    for i in adj[u]:
        if not visited[i]:
            index = euler_tree(i, index)
            euler[index] = u
            index += 1
    return index


def print_euler_tour(root, N):
    index = 0
    euler_tree(root, index)
    for i in range(2 * N - 1):
        print(euler[i], end=" ")


N = 4
add_edge(1, 2)
add_edge(2, 3)
add_edge(2, 4)

print_euler_tour(1, N)
