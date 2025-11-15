def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    for i in graph[start]:
        if i not in visited:
            dfs(graph, i, visited)
    return visited


graph = {

    'A': ['B', 'C'],
    'B': ['A'],
    'C': ['A'],
    'D': ['E'],
    'E': ['D'],
    'F': []
}
print(dfs(graph, 'D'))
