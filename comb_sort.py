"""
Comb Sort is mainly an improvement over Bubble Sort. Bubble sort always
compares adjacent values. Comb Sort improves on Bubble Sort by using gap of
size more than 1.
The shrink factor has been empirically found to be 1.3 (by testing Combsort on
over 200,000 random lists)
"""


def get_next_gap(gap):
    """
    To find next gap from current
    """
    # Shrink gap by Shrink factor
    gap = int((gap * 10) / 13)
    if gap < 1:
        return 1
    return gap


def sort(elements_list):
    """
    Function to sort arr[] using Comb Sort
    """
    size = len(elements_list)

    # Initialize gap
    gap = size

    # Initialize swapped as true to make sure that
    # loop runs
    swapped = True

    # Keep running while gap is more than 1 and last
    # iteration caused a swap
    while gap != 1 or swapped:

        # Find next gap
        gap = get_next_gap(gap)

        # Initialize swapped as false so that we can
        # check if swap happened or not
        swapped = False

        # Compare all elements with current gap
        for i in range(0, size - gap):
            if elements_list[i] > elements_list[i + gap]:
                elements_list[i], elements_list[i + gap] =\
                    elements_list[i + gap], elements_list[i]  # swap
                swapped = True

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
