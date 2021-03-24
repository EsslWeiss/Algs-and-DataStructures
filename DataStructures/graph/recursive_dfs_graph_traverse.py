import ipdb

# adj list
GRAPH = {
    0: {1, 2},
    1: {0, 3, 4},
    2: {0},
    3: {1, 5},
    4: {2, 3},

    5: {10, 2, 6},
    6: {10, 5, 7},
    7: {0, 1, 3},
}


def rec_dfs_traverse(graph, curr_vertex, visited=None):
    ipdb.set_trace()
    if not visited:
        visited = set()

    visited.add(curr_vertex)
    for neighbor_vertex in graph[curr_vertex] - visited:
        rec_dfs_traverse(graph, neighbor_vertex, visited)

    return visited


if __name__ == "__main__":
    print(rec_dfs_traverse(GRAPH, curr_vertex=3))

