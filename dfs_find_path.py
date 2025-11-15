def dfs(graph, start, end, visited=None, path=None):
    if path is None:
        path = list()
    path.append(start)

    if visited is None:
        visited = set()
    visited.add(start)

    if start == end:
        return path

    for i in graph[start]:
        if i not in visited:
            result = dfs(graph, i, end, visited, path)
            if result is not None:
                return result

    path.pop()
    return None


graph = {
    'A': ['B', 'C'],
    'B': ['A'],
    'C': ['A'],
    'D': ['E'],
    'E': ['D'],
    'F': []
}
print(dfs(graph, 'B', 'C'))
