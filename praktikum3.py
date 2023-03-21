graph = {
    0: [3, 4],
    1: [0, 6],
    2: [6, 5],
    3: [1, 7],
    4: [6],
    5: [6, 7],
    6: [2, 4],
    7: [5]
}

# Breadth First Search Algorithm
def bfs(graph, start):
    visited = []
    queue = [start]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            neighbors = graph[node]
            for neighbor in neighbors:
                queue.append(neighbor)
    return visited

# Depth First Search Algorithm
def dfs(graph, start, visited=None):
    if visited is None:
        visited = []
    visited.append(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited

# Menampilkan hasil Breadth First Search
print("Traversal dengan Breadth First Search:")
print(bfs(graph, 0))

# Menampilkan hasil Depth First Search
print("Traversal dengan Depth First Search:")
print(dfs(graph, 0))