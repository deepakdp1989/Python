"""
 Searching an element in a list/array in python  can be simply done using 'in'
 operator.
 Example:
 if x in arr:
 print arr.index(x)
 If you want to implement Linear Search in python
 Linearly search x in arr[]
 If x is present then return its location
 else return -1
"""


def search(elements_list, element):
    """ search element in list and return its position """
    for index, item in enumerate(elements_list):
        if item == element:
            return index
    return -1


def main():
    """
    Main. Running the code
    """
    print(search(range(1, 21, 2), 9))  # will print 4
    print(search(range(1, 21, 2), 0))  # will print -1


if __name__ == "__main__":
    main()
