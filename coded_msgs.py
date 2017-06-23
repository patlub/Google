def answer(l, t):
    """
    Decrypts messages l using numerical key t

    Arguments:
        l: A list of positive integers holding the encrypted message
        t: An integer representing the decryption key

    Returns:
        A list of the start and end index of the message sequence

    Raises:
        TypeError:
            l is not type list or t is n ot int
    """
    if not isinstance(l, list) or not isinstance(t, int):
        raise TypeError('l and t must be list and int respectively')

    elif not (all(isinstance(item, int) and item in range(1, 101) for item in l)):
        return 'All list items should be positive integers between 0 and 100'

    elif not l:
        return 'Broadcast cant be empty'

    elif len(l) > 100:
        return 'Broadcast more than 100 elements'

    elif not 250 >= t > 0:
        return 'key should be a positive integer between 0 and 250'

    else:
        # Loop through the sublists of l while
        # summing each of them and return indices
        # of list whose sum equals to t
        # Otherwise return [-1, -1]
        for i, k in enumerate(l):
            if k == t:
                return [i, i]
            n = i + 2
            while n <= len(l):
                sub = l[i:n]
                if sum(sub) == t:
                    return [i, n - 1]
                n += 1
        return [-1, -1]
