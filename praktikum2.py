# Implementasi graph
graph = {
    '1': {'2': 1, '3': 2},
    '2': {'4': 6, '5': 12},
    '3': {'4': 3, '6': 4},
    '4': {'5': 4, '7': 15, '8': 7, '6': 3},
    '5': {'7': 7},
    '6': {'8': 7, '9': 15},
    '7': {'9': 3},
    '8': {'9': 10},
    '9': {}
}

# Implementasi algoritma BFS
def bfs(graph, start, end):
    queue = [[start]]
    visited = set()

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node == end:
            return path

        if node not in visited:
            for adjacent in graph.get(node, {}):
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)

            visited.add(node)

    return None

# Implementasi algoritma DFS
def dfs(graph, start, end, visited=None, path=None):
    if visited is None:
        visited = set()

    if path is None:
        path = [start]

    visited.add(start)

    if start == end:
        return path

    for adjacent in graph.get(start, {}):
        if adjacent not in visited:
            new_path = list(path)
            new_path.append(adjacent)
            result = dfs(graph, adjacent, end, visited, new_path)

            if result is not None:
                return result

    return None

# Contoh penggunaan algoritma BFS dan DFS
home = '1'
office = '9'

print('Traversal BFS: ', bfs(graph, home, office))
print('Traversal DFS: ', dfs(graph, home, office))