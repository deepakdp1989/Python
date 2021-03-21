"""
TimSort is a sorting algorithm based on Insertion Sort and Merge Sort.

1. A stable sorting algorithm works in O(n Log n) time
2. Used in Java's Arrays.sort() as well as Python's sorted() and sort().
3. First sort small pieces using Insertion Sort, then merges the pieces using
   merge of merge sort.

The minrun number is determined based on the N, by the following
principles:

1. It shouldn't be too long as the minrun will later be subjected to
    insertion sort, which is effective for short runs.
2. It shouldn't be too short, as, the shorter the run, the more runs will
    have to be merged in the next step.
3. It would be good if (N \\ minrun) was a power of 2 (or close to it). This
    requirement results from the fact that the merge sort performs best on
    the runs of about the same length.
"""
from algorithms.sorting.insertion_sort import sort as in_sort
from algorithms.sorting.merge_sort import sort as mrg_sort


def get_min_run(size):
    """
    Take the six most significant bits out of N and add one, if the remaining
    least significant bits contain at least one off bit.
    """
    res = 0

    while size >= 64:
        res |= size & 1
        size >>= 1
    return size + res


def sort(elements_list):
    """
    Iterative Timsort function to sort the
    """
    length = len(elements_list)
    min_run = get_min_run(length)

    start = 0
    while start < length:
        # Sort individual subarrays of size min_run
        elements_list[start: min(start + min_run, length)] =\
            in_sort(elements_list[start: min(start + min_run, length)])
        start += min_run

    size = min_run
    while size < length:

        left = 0
        while left < length:

            right = min((left + 2 * size - 1), (length - 1))
            elements_list[left: right + 1] =\
                mrg_sort(elements_list[left: right + 1])
            left += 2 * size

        size = 2 * size

    return elements_list


def main():
    """
    Main. Running the code
    """
    list_of_elems = [99, -70, 10, 0, -53, -79, 25, -50, 98, 76, -6, 87,
                     62, 75, -31, -60, 27, 22, 1, 79, 18, 47, 33, 23,
                     -56, -63, 8, 35, 78, -4, 24, 90, 65, -16, -2, -23, 88,
                     -65, 56, -28, 21, 19, -71, -61, -68, -35, -40, 80, 17,
                     31, 30, 5, 42, -33, -86, -17, -25, 11, 20, -100, 4, -80,
                     28, 39, -14, -26, 94, -46, 91, -62, 40, -75, -90, -51,
                     -76, -64, -85, 44, -20, 36, 93, -24, 14, -41, 13, -18,
                     64, -49, 68, -98, 83, -43, -12, 85, 66, 52, -15, 59, -30,
                     -96, 69, 2, 81, -77, -47, -13, 16, 34, -55, 29, 26, 73,
                     -81, -67, -5, 53, 96, 38, -34, -69, -21, 49, -7, -54, -88,
                     58, 92, -72, 61, 48, -42, 95, -66, -39, -9, 15, -3, 57,
                     -82, 12, -89, -78, -27, 37, 71, -52, -22, -32, -58, 3, 32,
                     -29, -87, 43, 51, -99, 46, 41, 50, 74, 9, 63, 72, -8, -37,
                     84, -83, -44, -1, -93, 55, -97, -45, 89, 6, -74, -38, 7,
                     82, 67, -11, 70, 77, 54, -59, 100, 45, -57, 60, -92, 97,
                     -10, -19, -84, -91, -36, -94, -48, -95, 86, -73]

    print(sort(list_of_elems))
    # will print -100 to 100 sequentially


if __name__ == "__main__":
    main()
