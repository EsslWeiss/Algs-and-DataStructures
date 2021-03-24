import ipdb
from collections import deque

# adj list matrix representation
GRAPH = {
    0: {1, 2},
    1: {0, 3, 4},
    2: {0},
    3: {1, 5},
    4: {2, 3},

    5: {10, 2, 6},
    6: {10, 5, 7},
    7: {0, 1, 3},
    10: {0, 5, 6}
}

def bfs_traverse(graph, init_vertex):
    ipdb.set_trace()
    visited = [init_vertex]
    queue = deque([init_vertex])

    while queue:
        curr_vertex = queue.popleft()  # get vertex from left part

        for neighbor_vertex in graph[curr_vertex]:
            if neighbor_vertex not in visited:
                visited.append(neighbor_vertex)
                queue.append(neighbor_vertex)
    
    return visited


if __name__ == "__main__":
    visited_result = bfs_traverse(GRAPH, init_vertex=3)
    print(visited_result)

