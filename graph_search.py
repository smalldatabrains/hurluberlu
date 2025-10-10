from collection import queue

# dummy structure graph

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}


# deep first search, iterative version


def create_maze(width, height):
    pass


def visualize(algorithm):
    pass

def dfs(graph, start):
    stack=[start] # stack logic is LAST IN FIRST OUT
    visited = []

    while stack:
        node = stack.pop()
        print('Node: ',node)
        if node not in visited:
            visited.append(node)
            print('Visited: ',visited)
            print('Graph[node]',graph[node])
            stack.extend(graph[node])
    return visited

print(dfs(graph,'A'))

def bfs(graph, start):
    pass
