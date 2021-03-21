"""
QuickSort is a Divide and Conquer algorithm. It picks an element as pivot
and partitions the given array around the picked pivot.
"""


def sort(elements_list):
    """
    Using list comprehension
    """
    if not elements_list:
        return []

    pivot = elements_list[0]

    if len(elements_list) == 1:
        return [pivot]

    left = sort([elem for elem in elements_list[1:] if elem < pivot])
    right = sort([elem for elem in elements_list[1:] if elem >= pivot])

    return left + [pivot] + right


def main():
    """
    Main. Running the code
    """
    list_of_elems = [3, 178, 4, 101, 40, 44, 205, 89, 10, 112, 2, 45]

    print(sort(list_of_elems))
    # will print [2, 3, 4, 10, 40, 44, 45, 89, 101, 112, 178, 205]


if __name__ == "__main__":
    main()
