import ipdb

# Graph representation as an adjacency list
GRAPH = {
    0: {1, 2},
    1: {0, 3, 4},
    2: {0},
    3: {1, 5},
    4: {2, 3},

    5: {10, 2, 6},
    6: {10, 5, 7},
    7: {0, 1, 3},
    10: {5, 6}
}

# Using the data structure stack
def dfs_traverse(graph, init_vertex):
    visited = []
    stack = [init_vertex]

    while stack:
        curr_vertex = stack.pop()
        if curr_vertex in visited:
            continue
        
        visited.append(curr_vertex)
        for neighbor_vertex in graph[curr_vertex] - set(visited):
            stack.append(neighbor_vertex)

    return visited


if __name__ == "__main__":
    visited_result = dfs_traverse(GRAPH, init_vertex=3)
    print(visited_result)

