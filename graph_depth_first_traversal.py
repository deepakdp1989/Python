"""
Depth-first search (DFS) is an algorithm for traversing or searching tree or
graph data structures. One starts at the root (selecting some arbitrary node
as the root in the case of a graph) and explores as far as possible along
each branch before backtracking.
"""
from algorithms.graphs.graph import Graph


def traverse(ds_graph=Graph, node=0):
    """
    Function to return a DFS of graph
    """
    visited = [False] * ds_graph.vertices

    stack = []
    stack.append(node)

    visited[node] = True

    t_vertices = []
    while stack:
        node = stack.pop()
        t_vertices.append(node)

        for index in ds_graph.graph[node]:
            if not visited[index]:
                stack.append(index)
                visited[index] = True

    return t_vertices


def main():
    """
    Running the code
    """
    grph = Graph(vertices=7, is_directed=False)
    grph.add_edge(0, 2)
    grph.add_edge(0, 1)
    grph.add_edge(2, 5)
    grph.add_edge(5, 6)
    grph.add_edge(1, 4)
    grph.add_edge(4, 6)
    grph.add_edge(6, 3)

    print(traverse(grph, 3))
    print(grph)


if __name__ == "__main__":
    main()
