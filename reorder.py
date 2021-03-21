"""
If X and Y are 2 arrays of same length such that X[i] corresponds to Y[i] then
reorder X based on Y
"""


def reorder_by_sort(arr, arr_to_sort):
    """
    Reorder arr based on arr_to_sort
    when arr_to_sort is sorted
    """
    # ask what does * do?
    return list(zip(*sorted(zip(arr, arr_to_sort), key=lambda x: x[1])))


def reorder_by_position(arr, arr_index):
    """
    Reorder arr based on positions
    given in arr_index
    """
    return [arr[i] for i in arr_index]


def reorder_by_index(arr, arr_index):
    """
    Reorder arr based on indexes
    given in arr_index
    """
    return [x[0] for x in sorted(zip(arr, arr_index), key=lambda k: k[1])]


def main():
    """
    Running the code
    """
    arr = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
    arr_to_sort = [0, 1, 1, 0, 1, 2, 2, 0, 1]

    reordered_arr = reorder_by_sort(arr, arr_to_sort)

    print(reordered_arr)
    print(list(zip(reordered_arr[0], reordered_arr[1])))

    arr = [5, 1, 3, 0, 5, 8]
    arr_to_sort = [9, 2, 4, 6, 7, 9]

    reordered_arr = reorder_by_sort(arr, arr_to_sort)

    print(reordered_arr[0])
    print(reordered_arr[1])
    print(list(zip(reordered_arr[0], reordered_arr[1])))

    mylist = ['a', 'b', 'c', 'd', 'e']
    myorder = [3, 2, 0, 1, 4]

    print(reorder_by_position(mylist, myorder))
    print(reorder_by_index(mylist, myorder))


if __name__ == "__main__":
    main()
