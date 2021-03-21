"""
Bubble Sort is the simplest sorting algorithm that works by repeatedly
swapping the adjacent elements if they are in wrong order.
"""


def sort(elements_list):
    """
    Function always runs O(n^2) time even if the array is
    sorted. It can be optimized by stopping the algorithm
    if inner loop didn't cause any swap.
    """

    length_list = len(elements_list)
    swapped = False
    for index in range(length_list):
        swapped = False

        for sub_index in range(0, length_list - index - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if elements_list[sub_index] > elements_list[sub_index + 1]:
                elements_list[sub_index], elements_list[sub_index + 1] =\
                    elements_list[sub_index + 1], elements_list[sub_index]
                swapped = True

        if not swapped:
            break

    return elements_list


def main():
    """
    Main. Running the code
    """
    list_of_elems = [3, 178, 4, 101, 40, 44, 205, 89, 10, 112, 2, 45]

    print(sort(list_of_elems))
    # will print  [2, 3, 4, 10, 40, 44, 45, 89, 101, 112, 178, 205]


if __name__ == "__main__":
    main()
