"""
Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of
vertices such that for every directed edge uv, vertex u comes before v in the
ordering. Topological Sorting for a graph is not possible if the graph is not
a DAG.

A DAG has at least one vertex with in-degree 0 and one vertex with out-degree
0.
Proof: There's a simple proof to the above fact is that a DAG does not contain
a cycle which means that all paths will be of finite length. Now let S be the
longest path from u(source) to v(destination). Since S is the longest path
there can be no incoming edge to u and no outgoing edge from v, if this
situation had occurred then S would not have been the longest path =>
indegree(u) = 0 and outdegree(v) = 0

Algorithm:
Steps involved in finding the topological ordering of a DAG:

Step-1: Compute in-degree (number of incoming edges) for each of the vertex
present in the DAG and initialize the count of visited nodes as 0.

Step-2: Pick all the vertices with in-degree as 0 and add them into a queue
(Enqueue operation)

Step-3: Remove a vertex from the queue (Dequeue operation) and then.

Increment count of visited nodes by 1.
Decrease in-degree by 1 for all its neighboring nodes.
If in-degree of a neighboring nodes is reduced to zero, then add it to the
queue.

Step 4: Repeat Step 3 until the queue is empty.

Step 5: If count of visited nodes is not equal to the number of nodes in the
graph then the topological sort is not possible for the given graph.
"""
from algorithms.graphs.graph import Graph


def sort(ds_graph=Graph):
    """
    The function to do Topological Sort.
    Works only for Directed Acyclic Graph
    """
    in_degree = [0]*(ds_graph.vertices)

    # Traverse adjacency lists to fill indegrees of
    # vertices.  This step takes
    for i in range(ds_graph.vertices):
        for j in ds_graph.graph[i]:
            in_degree[j] += 1

    # Create an queue and enqueue all vertices with
    # indegree 0
    queue = []
    for i in range(ds_graph.vertices):
        if in_degree[i] == 0:
            queue.append(i)

    cnt = 0

    # Create a vector to store result (A topological
    # ordering of the vertices)
    top_order = []

    # One by one dequeue vertices from queue and enqueue
    # adjacents if indegree of adjacent becomes 0
    while queue:

        # Extract front of queue (or perform dequeue)
        # and add it to topological order
        upper = queue.pop(0)
        top_order.append(upper)

        # Iterate through all neighbouring nodes
        # of dequeued node u and decrease their in-degree
        # by 1
        for i in ds_graph.graph[upper]:
            in_degree[i] -= 1
            # If in-degree becomes zero, add it to queue
            if in_degree[i] == 0:
                queue.append(i)

        cnt += 1

    return top_order


def main():
    """
    Running the code
    """
    grph = Graph(vertices=7, is_directed=True)
    grph.add_edge(0, 1)
    grph.add_edge(0, 2)
    grph.add_edge(1, 2)
    grph.add_edge(2, 3)
    grph.add_edge(4, 3)
    grph.add_edge(4, 6)
    grph.add_edge(6, 5)

    print(grph)
    print(sort(grph))


if __name__ == "__main__":
    main()
