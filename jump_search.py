"""
Jump Search is a searching algorithm for sorted arrays by fixed steps or
skipping some elements in place of searching all elements

Consider the following array:
(0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610).
Length of the array is 16. Jump search will find the value of 55 with the
following steps assuming that the block size to be jumped is 4.
STEP 1: Jump from index 0 to index 4;
STEP 2: Jump from index 4 to index 8;
STEP 3: Jump from index 8 to index 16;
STEP 4: Since the element at index 16 is greater than 55 we
will jump back a step to come to index 9.
STEP 5: Perform linear search from index 9 to get the element 55.
"""
from algorithms.searching.linear_search import search as li_s
# Change this to 'import linear_search as li_s' for local run


def search(element_list_sorted, element):
    """
    Determinig the jump_step

    In the worst case, we have to do n/m jumps and if the
    last checked value is greater than the element to be
    searched for, we perform m-1 comparisons more for linear
    search. Therefore the total number of comparisons in the
    worst case will be ((n/m) + m-1). The value of the function
    ((n/m) + m-1) will be minimum when m = sqrt(n). Therefore, the
    best step size is m = sqrt(n).
    """

    length_list = len(element_list_sorted)

    jump_step = int(length_list ** (1 / 2.0))

    prev = 0
    # find the block where element is present
    # if it is present
    while element_list_sorted[min(jump_step, length_list) - 1] < element:
        prev = jump_step
        jump_step += jump_step
        if prev >= length_list:
            return -1

    return prev + li_s(element_list_sorted[prev:], element)


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


if __name__ == "__main__":
    main()
