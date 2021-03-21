"""
A disjoint-set data structure is a data structure that keeps track of a set of
elements partitioned into a number of disjoint (non-overlapping) subsets. A
union-find algorithm is an algorithm that performs two useful operations on
such a data structure:

Find: Determine which subset a particular element is in. This can be used for
determining if two elements are in the same subset.

Union: Join two subsets into a single subset.
"""
# pylint: disable=too-few-public-methods


class UnionFind(object):
    """
    Class that implements the union-find structure with
    union by rank and find with path compression

    :param size: Total number of elements in union set
    """

    def __init__(self, size):
        self.size = size
        self.parent = list(range(size))
        self.rank = [-1 for _ in range(size)]

    def find(self, elem):
        """
        The idea is to flatten the tree when find() is called.
        When find() is called for an elem, root of the
        tree is returned. The find() operation traverses up from
        elem to find root.
        This optimization is called Path Compression.
        The idea of path compression is to make the found root
        as parent of elem so that we don't have to traverse all
        intermediate nodes again. If elem is root of a subtree,
        then path (to root) from all nodes under elem also
        compresses.
        """
        if not elem == self.parent[elem]:
            self.parent[elem] = self.find(self.parent[elem])
        return self.parent[elem]

    def union(self, set1, set2):
        """
        Technically the rank is an upper bound for the height
        of a tree. The rank is not the height because during
        a find operation with path compression the height of
        a tree might become smaller, whereas the rank is not
        updated in the find function.
        Instead of simply linking the tree of set1 to the tree
        of set2, we will first compare their ranks. The tree
        with smaller rank is then linked to the tree with
        greater rank. This is called union by rank.
        """
        x_root = self.find(set1)
        y_root = self.find(set2)
        if x_root == y_root:
            return
        if self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[x_root] = y_root
            if self.rank[x_root] == self.rank[y_root]:
                self.rank[y_root] += 1

    def has_same_root(self, set1, set2):
        """
        Determine if elements have same root
        """
        x_root = self.find(set1)
        y_root = self.find(set2)
        return x_root == y_root

    def disjoint_sets(self):
        """
        Get all disjoint sets
        """
        my_dict = {}
        for node in range(self.size):
            root = self.find(node)
            if root not in my_dict:
                my_dict[root] = set([node])
            else:
                my_dict[root].add(node)

        return list(my_dict.values())

    def __str__(self):
        return "Index: "\
                + str(list(range(self.size)))\
                + "\n"\
                + "Parent: "\
                + "".join(str(self.parent))

    __repr__ = __str__


def main():
    """
    Running the code
    """
    # Part a)
    union_find = UnionFind(9)

    print("Initial Set:")
    print(union_find)

    union_find.union(2, 3)
    union_find.union(4, 3)
    union_find.union(6, 5)

    msg = (
        "\n"
        "Parent array after "
        "union(2, 1), "
        "union(4, 3) "
        "and union(6, 5):"
        )

    print(msg)
    print(union_find)
    print(union_find.has_same_root(2, 3))

    # Part b)
    union_find.union(2, 4)
    print("\nParent array after union(2, 4)")
    print(union_find)

    # Part c)
    union_find.find(2)
    print("\nParent array after find(2)")
    print(union_find)

    # Part d)
    print("\nDisjoint sets: ")
    print("\n".join([str(my_set) for my_set in union_find.disjoint_sets()]))


if __name__ == "__main__":
    main()
