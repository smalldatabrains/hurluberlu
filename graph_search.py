graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

# deep first search, iterative version

def dfs(graph, start):
    stack=[start] # stack logic is LAST IN FIRST OUT
    visited = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(graph[node])
    return visited

print(dfs(graph,'A'))

