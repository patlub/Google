def answer(l, t):
    sublists = []
    for i in range(len(l)):
        n = i + 2
        while n <= len(l):
            sub = l[i:n]
            sublists.append(sub)
            n += 1

    return sublists
