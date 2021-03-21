"""
Graph is a data structure that consists of following two components:
1. A finite set of vertices also called as nodes.
2. A finite set of ordered pair of the form (u, v) called as edge. The pair is
ordered because (u, v) is not same as (v, u) in case of directed
graph(di-graph). The pair of form (u, v) indicates that there is an edge from
vertex u to vertex v. The edges may contain weight/value/cost.
"""
from collections import defaultdict
from algorithms.disjoint_sets.union_find import UnionFind
# pylint: disable=too-few-public-methods


class Graph(object):
    """
    A representation for connected graph data structure using
    adjacency list
    :param vertices: No. of vertices
    :param is_directed: Indicate if graph is directed or un-directed
    :param is_cyclic: Indicate if graph is cyclic
    :param is_weighted: Indicate if graph edges has weights assigned to them.
    """

    def __init__(self, vertices=0, is_directed=False):
        self.vertices = vertices
        self.is_directed = is_directed
        self.graph = defaultdict(list)
        self.union_find = UnionFind(self.vertices)
        self.is_cyclic = False
        self.is_weighted = False
        self.weights = {}

    def add_edge(self, start, end, weight=None):
        """
        add an edge to graph
        """
        if self.is_directed:
            self.graph[start].append(end)
        else:
            self.graph[start].append(end)
            self.graph[end].append(start)

        if weight is not None:
            self.weights[(start, end)] = weight
            self.is_weighted = True

        def check_cycle():
            """
            check for cycle in graph
            """
            # No need to check for cycle if cycle is already detected
            if not self.is_cyclic:
                if not self.is_directed:
                    set1 = self.union_find.find(start)
                    set2 = self.union_find.find(end)
                    if set1 == set2:
                        self.is_cyclic = True
                        return
                    self.union_find.union(set1, set2)
                else:
                    visited = set()
                    path = [object()]
                    path_set = set(path)
                    stack = [iter(self.graph)]
                    while stack:
                        for vertex in stack[-1]:
                            if vertex in path_set:
                                self.is_cyclic = True
                                return
                            elif vertex not in visited:
                                visited.add(vertex)
                                path.append(vertex)
                                path_set.add(vertex)
                                stack.append(iter(self.graph.get(vertex, ())))
                                break
                        else:
                            path_set.remove(path.pop())
                            stack.pop()
        check_cycle()

    def __str__(self):

        v_set = set().union(
            [nodes for nodes in self.graph],
            [node for nodes in self.graph for node in self.graph[nodes]]
            )

        edges = set([(node1, node2)
                     for node1 in self.graph
                     for node2 in self.graph[node1]])

        return "\n".join([
            "Vertices: " + str(v_set),
            "Edges: " + str(edges),
            "Weights: " + str(self.weights),
            "Is Directed: " + str(self.is_directed),
            "Is Cyclic: " + str(self.is_cyclic),
            "Is Weighted: " + str(self.is_weighted)
            # "basic Cycles: " + str(self.basic_cycles())
        ])

    __repr__ = __str__


def main():
    """
    Running the code
    """
    grph = Graph(vertices=7, is_directed=True)
    grph.add_edge(0, 1, 4)
    grph.add_edge(0, 2, -5)
    grph.add_edge(1, 4, 3)
    grph.add_edge(4, 5, 2)
    grph.add_edge(5, 6, -2)
    grph.add_edge(2, 3, 1)
    grph.add_edge(4, 0, 7)

    print(grph)
    print(grph.graph)


if __name__ == "__main__":
    main()
