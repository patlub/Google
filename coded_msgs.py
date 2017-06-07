def answer(l, t):
    """Decrypts messages l using numerical key t

    :param l:
    :param t:
    :return:
    """
    if not isinstance(l, list) or not isinstance(t, int):
        raise TypeError('l and t must be list and int respectively')

    elif not (all(isinstance(item, int) and item > 0 for item in l)):
        return 'All list items should be positive integers'

    elif not t > 0:
        return 'key should be a positive integer'

    else:

        for i in range(len(l)):
            n = i + 2
            while n <= len(l):
                sub = l[i:n]
                if sum(sub) == t:
                    return [i, n - 1]
                n += 1
        return [-1, -1]

# a = [4, 3, 10, 2, 8]
# print(answer(a, 12))
