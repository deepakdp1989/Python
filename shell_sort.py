"""
ShellSort is mainly a variation of Insertion Sort. In insertion sort, we move
elements only one position ahead. When an element has to be moved far ahead,
many movements are involved. The idea of shellSort is to allow exchange of far
items. In shellSort, we make the array h-sorted for a large value of h. We
keep reducing the value of h until it becomes 1. An array is said to be
h-sorted if all sublists of every h'th element is sorted.
"""


def sort(elements_list):
    """
    Python program for implementation of Shell Sort
    """
    # Start with a big gap, then reduce the gap
    size = len(elements_list)
    gap = int(size / 2)

    # Do a gapped insertion sort for this gap size.
    # The first gap elements a[0..gap-1] are already in gapped
    # order keep adding one more element until the entire array
    # is gap sorted
    while gap > 0:

        for i in range(gap, size):

            # add a[i] to the elements that have been gap sorted
            # save a[i] in temp and make a hole at position i
            temp = elements_list[i]

            # shift earlier gap-sorted elements up until the correct
            # location for a[i] is found
            j = i
            while j >= gap and elements_list[j - gap] > temp:
                elements_list[j] = elements_list[j - gap]
                j -= gap

            # put temp (the original a[i]) in its correct location
            elements_list[j] = temp
        gap = int(gap / 2)

    return elements_list


def main():
    """
    Main. Running the code
    """
    list_of_elems = [3, 178, 4, 101, 40, 44, 205, 89, 10, 112, 2, 45]

    print(sort(list_of_elems))
    # will print [2, 3, 4, 10, 40, 44, 45, 89, 101, 112, 178, 205]


if __name__ == "__main__":
    main()
