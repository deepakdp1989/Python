"""
The idea is to start with subarray size 1 compare its last element with x,
then try size 2, then 4 and so on until last element of a subarray is not
greater. Once we find an index i (after repeated doubling of i), we know that
the element must be present between i/2 and i (Why i/2? because we could not
find a greater value in previous iteration)
"""
from algorithms.searching.binary_search import iterative_search as bi_s
# Change this to 'import binary_search as bi_s' for local run


def search(element_list_sorted, element):
    """
    Exponential search involves two steps:

    1. Find range where element is present
    2. Do Binary Search in above found range.
    """
    length_list = len(element_list_sorted)

    if element_list_sorted[0] == element:
        return 0

    index = 1
    while index < length_list and\
            element_list_sorted[index] <= element:
        index *= 2

    binary_search_result = bi_s(
        element_list_sorted[(int(index / 2)): min(index, length_list)], element
        )
    return (int(index / 2)) + binary_search_result\
        if binary_search_result != -1 else -1


def main():
    """
    Main. Running the code
    """
    list_of_elems = [0, 1, 1, 2, 3, 5, 8, 13, 21,
                     34, 55, 89, 144, 233, 377, 610, 987]

    print(search(list_of_elems, 144))  # will print 12
    print(search(list_of_elems, 165415))  # will print -1
    print(search(list_of_elems, 13))  # will print 7
    print(search(list_of_elems, 987))  # will print 16
    print(search(list_of_elems, -232))  # will print -1
    print(search(list_of_elems[0:1], 0))  # will print 0


if __name__ == "__main__":
    main()
