"""
Write a function answer(l) that takes a list of positive integers
l and counts the number of "lucky triples" of (lst[i], lst[j], 
lst[k]) where i < j < k.  The length of l is between 2 and 2000 inclusive.
The elements of l are between 1 and 999999 inclusive.  The answer fits
within a signed 32-bit integer. Some of the lists are purposely generated
without any access codes to throw off spies, so if no triples are found,
return 0.
"""


def answer(l):
    """
    Returns the number of lucky triples in list l
    Args:
        list l: list of positive integers
    Raises:
        TypeError: if l is not list
    Returns:
        int: Number of lucky triples in list
    """
    if not isinstance(l, list):
        raise TypeError('Argument l should be a list')
    elif not len(l) in range(2, 2001):
        return 'Arg list length is out of acceptable range'
    elif [i for i in l if i not in range(1, 1000000)]:
        return 'Arg list contains elements outside acceptable range'

    lucky_triples = 0
    size = len(l)
    if size < 3: return 0

    cache = [0] * size
    for x in range(size):
        for y in range(x + 1, size):
            if l[y] % l[x] == 0:
                cache[y] += 1
                lucky_triples += cache[x]

    return lucky_triples


l = [1, 2, 3, 4, 5, 6]
m = [1, 3, 5, 7, 11, 13]
d = [4, 5, 2, 8, 5, 9, 2, 2, 7, 1]
c = [1, 2, 4, 8]
a = [1, 1, 1]
# print(c[2:])
print(answer(d))
print(answer(a))
