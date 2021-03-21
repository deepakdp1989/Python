"""
The idea of Radix Sort is to do digit by digit sort starting from least
significant digit to most significant digit. Radix sort uses counting sort as
a subroutine to sort.
"""


def count_sort(elements_list, exponent):
    """
    A function to do counting sort of arr[] according to
    the digit represented by exponent.
    """
    size = len(elements_list)

    # The output array elements that will have sorted arr
    output = [0] * (size)

    # initialize count array as 0
    count = [0] * (10)

    # Store count of occurrences in count[]
    for pos in range(0, size):
        index = (int(elements_list[pos] / exponent))
        count[(index) % 10] += 1

    # Change count[i] so that count[i] now contains actual
    # position of this digit in output array
    for pos in range(1, 10):
        count[pos] += count[pos - 1]

    # Build the output array
    pos = size - 1
    while pos >= 0:
        index = int((elements_list[pos] / exponent))
        output[count[(index) % 10] - 1] = elements_list[pos]
        count[(index) % 10] -= 1
        pos -= 1

    # Copying the output array to elements_list[],
    # so that elements_list now contains sorted numbers
    pos = 0
    for pos in range(0, len(elements_list)):
        elements_list[pos] = output[pos]


def sort(elements_list):
    """
    Method to do Radix Sort
    """
    # Find the maximum number to know number of digits
    max_value = max(elements_list)

    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exponent = 1
    while max_value / exponent > 0:
        count_sort(elements_list, exponent)
        exponent *= 10

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
