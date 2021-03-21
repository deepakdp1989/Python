"""
This algorithm finds all occurrences of a pattern in a text in linear time. Let
length of text be n and of pattern be m, then total time taken is O(m + n) with
linear space complexity.
"""


def z_array(text):
    """
    For a string str[0..n-1], Z array is of same length as string.
    An element z_arr[i] of Z array stores length of the longest
    substring starting from str[i] which is also a prefix of
    str[0..n-1]. The first entry of Z array is meaning less as
    complete string is always prefix of itself.

    Example:
    Index   : 0   1   2   3   4   5   6   7   8   9  10  11
    Text    : a   a   b   c   a   a   b   x   a   a   a   z
    Z values: X   1   0   0   3   1   0   0   2   2   1   0
    """
    z_arr = [0] * len(text)
    z_arr[0] = len(text)

    r_t = 0
    l_t = 0

    for idx in range(1, len(text)):
        if idx > r_t:
            # If idx is outside the current Z-box, do naive computation.
            pos = 0
            while pos + idx < len(text) and text[pos] == text[pos + idx]:
                pos += 1
            z_arr[idx] = pos
            if pos > 0:
                l_t = idx
                r_t = idx + pos - 1
        else:
            # If idx is inside the current Z-box, consider two cases.

            pair_idx = idx - l_t  # Pair index.
            right_part_len = r_t - idx + 1

            if z_arr[pair_idx] < right_part_len:
                z_arr[idx] = z_arr[pair_idx]
            else:
                i = r_t + 1
                while i < len(text) and text[i] == text[i - idx]:
                    i += 1
                z_arr[idx] = i - idx

                l_t = idx
                r_t = i - 1
    return z_arr


def search_with_sentinel(pattern, text):
    """
    Take a string T (for "text") and a string P (for "pattern"),
    both built of characters of some alphabet A. Also, take
    character '$' which is not in A. This character is called
    the sentinel. Assemble all these things in the following way: P$T
    """
    result = []

    z_search = z_array('{0}${1}'.format(pattern, text))
    for idx, z_val in enumerate(z_search):
        if z_val == len(pattern):
            result.append(idx - len(pattern) - 1)

    return result


def search(pattern, text):
    """
    For a general-purpose use the choice of the sentinel can be
    restrictive. Fortunately, there is search algorithm that
    doesn't need to use sentinels. The idea is in calculating
    Z-values of a string PT with a simple modification: after
    each Z-value is calculated, limit it to the |P|, i.e., Zk :=
    min{|P|, Zk}. This limitation plays role of the sentinel.
    """
    str_search = pattern + text
    z_arr = [0] * len(str_search)
    z_arr[0] = len(str_search)

    r_t = 0
    l_t = 0

    occurrence = []

    for idx in range(1, len(str_search)):
        if idx > r_t:
            pos = 0
            while pos + idx < len(str_search) and\
                    str_search[pos] == str_search[pos + idx]:
                pos += 1
            z_arr[idx] = pos
            if pos > 0:
                l_t = idx
                r_t = idx + pos-1
        else:
            pair_idx = idx - l_t
            right_part_len = r_t - idx + 1

            if z_arr[pair_idx] < right_part_len:
                z_arr[idx] = z_arr[pair_idx]
            else:
                i = r_t + 1
                while i < len(str_search) and\
                        str_search[i] == str_search[i - idx]:
                    i += 1
                z_arr[idx] = i - idx

                l_t = idx
                r_t = i - 1

        z_arr[idx] = min(len(pattern), z_arr[idx])

        # An occurence found.
        if z_arr[idx] == len(pattern):
            occurrence.append(idx - len(pattern))

    return occurrence


def main():
    """
    Running the code
    """
    print(search_with_sentinel("ab", "abcxxxabyyy"))
    print(search("ab", "abcxxxabyyy"))
    print(z_array("ab$abcxxxabyyy"))
    print(z_array("aab$baabaa"))
    print(z_array("aaaaaa"))
    print(z_array("aabaacd"))
    print(z_array("abababab"))


if __name__ == "__main__":
    main()
