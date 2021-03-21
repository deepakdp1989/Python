"""
Breadth-first traversal/search (BFS) is an algorithm for traversing/searching
graph data structures. It starts at the tree root (or some arbitrary node of a
graph, sometimes referred to as a 'search key') and explores the neighbor
nodes first, before moving to the next level neighbours.
"""
from algorithms.graphs.graph import Graph


def traverse(ds_graph=Graph, node=0):
    """
    Function to return a BFS of graph
    """
    visited = [False] * ds_graph.vertices

    queue = []
    queue.append(node)

    visited[node] = True

    t_vertices = []
    while queue:
        node = queue.pop(0)
        t_vertices.append(node)

        for index in ds_graph.graph[node]:
            if not visited[index]:
                queue.append(index)
                visited[index] = True

    return t_vertices


def main():
    """
    Running the code
    """
    grph = Graph(vertices=7, is_directed=True)
    # grph.add_edge(0, 1)
    # grph.add_edge(1, 2)
    # grph.add_edge(2, 5)
    # grph.add_edge(1, 6)
    # grph.add_edge(1, 4)
    # grph.add_edge(2, 3)
    grph.add_edge(0, 1)
    grph.add_edge(0, 2)
    grph.add_edge(1, 2)
    grph.add_edge(2, 0)
    grph.add_edge(2, 3)
    grph.add_edge(3, 3)
    grph.add_edge(5, 4)
    grph.add_edge(4, 6)
    grph.add_edge(6, 5)

    print(traverse(grph, 6))
    print(grph)


if __name__ == "__main__":
    main()
