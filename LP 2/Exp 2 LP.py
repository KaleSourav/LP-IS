import queue as Q

# Heuristic values
h = {
    'A': 13, 'C': 12, 'E': 11, 'G': 10, 'I': 9,
    'K': 8, 'M': 7, 'N': 6, 'P': 5, 'R': 4,
    'T': 3, 'U': 2, 'V': 1, 'B': 0
}

# Graph with 13 moves
graph = {
    'A': {'C': 4},
    'C': {'E': 6},
    'E': {'G': 5},
    'G': {'I': 7},
    'I': {'K': 4},
    'K': {'M': 8},
    'M': {'N': 3},
    'N': {'P': 6},
    'P': {'R': 5},
    'R': {'T': 7},
    'T': {'U': 4},
    'U': {'V': 6},
    'V': {'B': 5},
    'B': {}
}

start = 'A'
goal = 'B'

def fn(path):
    nodes = path.split(" -> ")
    g = 0
    for i in range(len(nodes) - 1):
        g += graph[nodes[i]][nodes[i + 1]]
    return g + h[nodes[-1]]

def astar():
    pq = Q.PriorityQueue()
    pq.put((fn(start), start, start))
    visited = set()

    while not pq.empty():
        cost, path, node = pq.get()

        if node == goal:
            moves = len(path.split(" -> ")) - 1
            print("Goal state reached")
            print("Path:", path)
            print("Total cost:", cost)
            print("Number of moves =", moves)
            return

        if node in visited:
            continue
        visited.add(node)

        for nxt in graph[node]:
            new_path = path + " -> " + nxt
            pq.put((fn(new_path), new_path, nxt))

astar()