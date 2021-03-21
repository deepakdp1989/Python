"""
Sort an arr[] of size n
insertionSort(arr, n)
Loop from i = 1 to n-1.
Pick element arr[i] and insert it into sorted sequence arr[0...i-1]
"""


def sort(elements_list):
    """
    Traverse through 1 to len(elements_list)

    Move elements of elements_list[0..i-1], that are
    greater than key, to one position ahead of their
    current position.
    """
    for index in range(1, len(elements_list)):
        key = elements_list[index]

        sub_index = index - 1
        while sub_index >= 0 and key < elements_list[sub_index]:
            elements_list[sub_index + 1] = elements_list[sub_index]
            sub_index -= 1

        elements_list[sub_index + 1] = key

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
