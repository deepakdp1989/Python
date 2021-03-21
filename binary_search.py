"""
Search a sorted array by repeatedly dividing the search interval in half. Begin
with an interval covering the whole array. If the value of the search key is
less than the item in the middle of the interval, narrow the interval to the
lower half. Otherwise narrow it to the upper half. Repeatedly check until the
value is found or the interval is empty.
"""


def iterative_search(elements_list_sorted, element):
    """
    Iterative Binary Search Function
    It returns location of x in given array arr if present,
    else returns -1
    """
    index_start = 0
    index_last = len(elements_list_sorted) - 1

    while index_start <= index_last:

        index_mid = index_start + int((index_last - index_start) / 2)

        if elements_list_sorted[index_mid] == element:
            # Check if element is present at mid
            return index_mid
        elif elements_list_sorted[index_mid] < element:
            # If element is greater, ignore left half
            index_start = index_mid + 1
        else:
            # If element is smaller, ignore right half
            index_last = index_mid - 1

    # If we reach here, then the element was not present
    return -1


def recursive_search(elements_list_sorted, element):
    """
    Recursive Binary Search Function
    It returns location of x in given array arr if present,
    else returns -1
    """
    def recurse(first, last):
        """
        Recursive part of the algorithm
        """
        mid = int((first + last) / 2)
        index = 0

        if first > last:
            index = -1

        elif elements_list_sorted[mid] < element:
            index = recurse(mid + 1, last)

        elif elements_list_sorted[mid] > element:
            index = recurse(first, mid - 1)

        else:
            index = mid

        return index

    return recurse(0, len(elements_list_sorted)-1)


def main():
    """
    Main. Running the code
    """
    list_of_elems = [2, 3, 4, 10, 40, 44, 45, 89, 101, 112, 178, 205]

    print(iterative_search(list_of_elems, 101))  # will print 8
    print(iterative_search(list_of_elems, 300))  # will print -1
    print(iterative_search(list_of_elems, -254645))  # will print -1
    print(iterative_search(list_of_elems, 2))  # will print 0
    print(recursive_search(list_of_elems, 178))  # will print 10
    print(recursive_search(list_of_elems, 1616164))  # will print -1
    print(recursive_search(list_of_elems, 10))  # will print 3
    print(recursive_search(list_of_elems[0:2], -8451854))  # will print -1


if __name__ == "__main__":
    main()
