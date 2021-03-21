"""
Heap sort is a comparison based sorting technique based on Binary Heap data
structure. It is similar to selection sort where we first find the maximum
element and place the maximum element at the end. We repeat the same process
for remaining element.
"""


def max_heapify(elements_list, heap_size, index):
    """
    Heapify procedure can be applied to a node only if its children nodes
    are heapified.
    1. Build a max heap from the input data.
    2. At this point, the largest item is stored at the root of the heap.
       Replace it with the last item of the heap followed by reducing the
       size of heap by 1. Finally, heapify the root of tree.
    3. Repeat above steps while size of heap is greater than 1.
    """
    largest = index  # Initialize largest as root
    left = 2 * index + 1
    right = 2 * index + 2

    # See if left child of root exists and is
    # greater than root
    if left < heap_size and\
            elements_list[index] < elements_list[left]:
        largest = left

    # See if right child of root exists and is
    # greater than root
    if right < heap_size and\
            elements_list[largest] < elements_list[right]:
        largest = right

    # Change root, if needed
    if largest != index:
        elements_list[index], elements_list[largest] =\
            elements_list[largest], elements_list[index]  # swap

        # Heapify the root.
        max_heapify(elements_list, heap_size, largest)


def sort(elements_list):
    """
    A Binary Heap is a Complete Binary Tree where items are stored in a
    special order such that value in a parent node is greater(or smaller)
    than the values in its two children nodes. The former is called as max
    heap and the latter is called min heap. The heap can be represented by
    binary tree or array.
    """
    heap_size = len(elements_list)

    # Build a maxheap.
    for index in range(heap_size, -1, -1):
        max_heapify(elements_list, heap_size, index)

    # One by one extract elements
    for index in range(heap_size - 1, 0, -1):

        elements_list[index], elements_list[0] =\
            elements_list[0], elements_list[index]   # swap

        max_heapify(elements_list, index, 0)

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
