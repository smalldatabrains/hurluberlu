graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def dfs(graph, start):
    stack=[start]
    visited = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            
