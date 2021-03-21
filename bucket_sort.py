"""
Bucket sort is mainly useful when input is uniformly distributed over a range.
The hash function that is used to partition the elements need to be very good
and must produce ordered hash: if i < k then hash(i) < hash(k).
The particular distinction for bucket sort is that it uses a hash function to
partition the keys of the input array, so that multiple keys may hash to the
same bucket. Hence each bucket must effectively be a growable list; similar to
radix sort.
"""
from algorithms.sorting.insertion_sort import sort as in_sort
# Change this to 'import insertion_sort as in_sort' for local run


def hashing(elements_list):
    """
    hashing for buckets
    """
    left = elements_list[0]
    for pos in range(1, len(elements_list)):
        if left < elements_list[pos]:
            left = elements_list[pos]
    result = [left, int(len(elements_list) ** 0.5)]
    return result


def re_hashing(index, code):
    """
    re_hashing to get the bucket position
    """
    return int(index / code[0] * (code[1] - 1))


def sort(elements_list):
    """
    Function to sort arr[] of size n using bucket sort
    Insertionsort is used to sort each bucket. This is
    to inculcate that the bucket sort algorithm does not
    specify which sorting technique to use on the buckets.
    """
    code = hashing(elements_list)

    buckets = [list() for _ in range(code[1])]

    for index in elements_list:
        bucket_pos = re_hashing(index, code)
        buckets[bucket_pos].append(index)

    for bucket in buckets:
        bucket = in_sort(bucket)

    pos = 0
    for bucket_pos, _ in enumerate(buckets):
        for value in buckets[bucket_pos]:
            elements_list[pos] = value
            pos += 1

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
