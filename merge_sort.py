"""
Merge Sort is a Divide and Conquer algorithm. It divides input array in two
halves, calls itself for the two halves and then merges the two sorted halves.
"""


def sort(elements_list):
    """
    Time complexity of Merge Sort is Q(nLogn) in all 3 cases (worst,
    average and best) as merge sort always divides the array in two
    halves and take linear time to merge two halves.
    """
    if len(elements_list) > 1:

        mid = len(elements_list) // 2

        lefthalf = elements_list[:mid]
        righthalf = elements_list[mid:]

        sort(lefthalf)
        sort(righthalf)

        ini_left_idx = 0
        ini_right_idx = 0
        ini_merge_idx = 0

        while ini_left_idx < len(lefthalf) and ini_right_idx < len(righthalf):
            if lefthalf[ini_left_idx] < righthalf[ini_right_idx]:
                elements_list[ini_merge_idx] = lefthalf[ini_left_idx]
                ini_left_idx += 1
            else:
                elements_list[ini_merge_idx] = righthalf[ini_right_idx]
                ini_right_idx += 1
            ini_merge_idx += 1

        while ini_left_idx < len(lefthalf):
            elements_list[ini_merge_idx] = lefthalf[ini_left_idx]
            ini_left_idx += 1
            ini_merge_idx += 1

        while ini_right_idx < len(righthalf):
            elements_list[ini_merge_idx] = righthalf[ini_right_idx]
            ini_right_idx += 1
            ini_merge_idx += 1

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
