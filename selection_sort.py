"""
The selection sort algorithm sorts an array by repeatedly finding the minimum
element (considering ascending order) from unsorted part and putting it at the
beginning.
"""


def sort(elements_list):
    """
    In every iteration of selection sort, the minimum element
    (considering ascending order) from the unsorted subarray
    is picked and moved to the sorted subarray.
    """
    for index, _ in enumerate(elements_list):

        # Find the minimum element in remaining
        # unsorted array
        min_idx = index
        for sub_indx in range(index + 1, len(elements_list)):
            if elements_list[min_idx] > elements_list[sub_indx]:
                min_idx = sub_indx

        # Swap the found minimum element with
        # the first element of sub array
        elements_list[index], elements_list[min_idx] =\
            elements_list[min_idx], elements_list[index]

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
