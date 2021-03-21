"""
Given a sorted array of n uniformly distributed values arr[], search for a
particular element x in the array.
Interpolation search may go to different locations according the value of key
being searched. For example if the value of key is closer to the last element,
interpolation search is likely to start search toward the end side.

To find the position to be searched, it uses following formula.
The idea of formula is to return higher value of pos when element to be
searched is closer to arr[hi] and smaller value when closer to arr[lo]

pos = lo + [ (x-arr[lo])*(hi-lo) / (arr[hi]-arr[Lo]) ]
arr[] ==> Array where elements need to be searched
x     ==> Element to be searched
lo    ==> Starting index in arr[]
hi    ==> Ending index in arr[]
"""


def search(element_list_sorted, element):
    """
    If element is present in element_list_sorted[0..n-1],
    then returns index of it, else returns -1
    """
    length_list = len(element_list_sorted)
    index_start = 0
    index_last = length_list - 1

    while index_start <= index_last and\
        element >= element_list_sorted[index_start] and\
            element <= element_list_sorted[index_last]:

        index = (
            # pos = lo + [ (x-arr[lo])*(hi-lo) / (arr[hi]-arr[Lo]) ]
            index_start +
            int(
                (
                    (element - element_list_sorted[index_start]) *
                    (index_last - index_start)
                ) /
                float((
                    element_list_sorted[index_last] -
                    element_list_sorted[index_start]
                ))
            ))

        if element_list_sorted[index] == element:
            return index
        if element_list_sorted[index] < element:
            index_start = index + 1
        else:
            index_last = index - 1

    return -1


def main():
    """
    Main. Running the code
    """
    list_of_elems = [10, 12, 13, 16, 18, 19, 20, 21, 22,
                     23, 24, 33, 35, 42, 47]
    print(search(list_of_elems, 18))  # will print 4
    print(search(list_of_elems, 47))  # will print 14
    print(search(list_of_elems, 10))  # will print 0
    print(search(list_of_elems, 33))  # will print 11
    print(search(list_of_elems, 1))  # will print -1
    print(search(list_of_elems, 300))  # will print -1


if __name__ == "__main__":
    main()
