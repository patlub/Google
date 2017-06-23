"""
Doomsday Fuel
=============

Write a function answer(m) that takes an array of array of nonnegative
ints representing how many times that state has gone to the next state
and return an array of ints for each terminal state giving the exact 
probabilities of each terminal state, represented as the numerator for 
each state, then the denominator for all of them at the end and in 
simplest form. The matrix is at most 10 by 10. It is guaranteed that 
no matter which state the ore is in, there is a path from that state 
to a terminal state. That is, the processing will always eventually end 
in a stable state. The ore starts in state 0. The denominator will fit 
within a signed 32-bit integer during the calculation, as long as the 
fraction is simplified regularly.
"""


def answer(m):
    """
    Returns an array of ints for each terminal state
    giving the exact probabilities of each terminal state
    Args:
        m: A matrix(list of lists) representing the different
           states of the ore
    Raises:
        TypeError: If m is not a matrix(list of lists)
    Returns:
        list: Probabilities of each terminal state
    """

    if not isinstance(m, list) or not all(isinstance(l, list) for l in m):
        raise TypeError('Argument should be a matrix(List of lists)')

    elif len(m) not in range(1, 11):
        return 'Matrix elements out of acceptable range(10 X 10)'

    for array in m:
        if len(array) not in range(1, 11):
            return 'Inner list out of acceptable range(10)'
        elif not all(isinstance(i, int) for i in array):
            return 'Matrix should not contain non integers'
        elif not all(i >= 0 for i in array):
            return 'List should not contain negatives'

    term_states = []
    non_term_states = []
    ordered_non_term_states = []
    term_pos = []
    non_term_pos = []
    for i in range(len(m)):
        if max(m[i]) is 0:
            term_states.append(m[i])
            term_pos.append(i)
        else:
            non_term_states.append(m[i])
            non_term_pos.append(i)

    init_pos = term_pos + non_term_pos

    off_sets = []
    for i in range(len(init_pos)):
        for j, a in enumerate(init_pos):
            if i == a:
                off_sets.append(j)

    for i in non_term_states:
        b = [k for k in range(len(i))]
        for j, a in enumerate(off_sets):
            b[a] = i[j]
        ordered_non_term_states.append(b)

    print(term_states + ordered_non_term_states)


m = [
    [0, 1, 0, 0, 0, 1],  # s0, the initial state, goes to s1 and s5 with equal probability
    [4, 0, 0, 3, 2, 0],  # s1 can become s0, s3, or s4, but with different probabilities
    [0, 0, 0, 0, 0, 0],  # s2 is terminal, and unreachable (never observed in practice)
    [0, 0, 0, 0, 0, 0],  # s3 is terminal
    [0, 0, 0, 0, 0, 0],  # s4 is terminal
    [0, 0, 0, 0, 0, 0],  # s5 is terminal
]

print(answer(m))
