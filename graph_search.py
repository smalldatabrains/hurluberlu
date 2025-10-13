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


def generate_maze(width, height):
    """
    Generate maze as a grid using recursive DFS.
    Returns:
        maze_walls: dict mapping (x, y) -> {'N': bool, 'S': bool, 'E': bool, 'W': bool}
                    True means wall exists, False means open passage.
    """
    # Initialize all walls as present
    maze_walls = {(x, y): {'N': True, 'S': True, 'E': True, 'W': True}
                  for y in range(height) for x in range(width)}

    directions = {
        'N': (0, -1, 'S'),
        'S': (0, 1, 'N'),
        'E': (1, 0, 'W'),
        'W': (-1, 0, 'E')
    }

    visited = set()

    def dfs(x, y):
        visited.add((x, y))
        dirs = list(directions.keys())
        random.shuffle(dirs)
        for d in dirs:
            dx, dy, opposite = directions[d]
            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height and (nx, ny) not in visited:
                # remove wall between (x,y) and (nx,ny)
                maze_walls[(x, y)][d] = False
                maze_walls[(nx, ny)][opposite] = False
                dfs(nx, ny)

    dfs(0, 0)
    return maze_walls


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
