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
import operator
from copy import deepcopy
from fractions import Fraction
from functools import reduce


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
        elif len(m) is 1:
            return [1, 1]

    ordered_non_term_states = []
    term_states = [m[i] for i in range(len(m)) if max(m[i]) is 0]
    term_pos = [i for i in range(len(m)) if max(m[i]) is 0]
    non_term_states = [m[i] for i in range(len(m)) if max(m[i]) is not 0]
    non_term_pos = [i for i in range(len(m)) if max(m[i]) is not 0]

    init_pos = term_pos + non_term_pos

    off_sets = []
    for i in range(len(init_pos)):
        for j, a in enumerate(init_pos):
            if i == a:
                off_sets.append(j)

    for i in non_term_states:
        b = [k is 0 for k in range(len(i))]
        for j, a in enumerate(off_sets):
            b[a] = i[j]
        ordered_non_term_states.append(b)

    probs = [[Fraction(j, sum(i)) for j in i] for i in ordered_non_term_states]
    sub_matrix_1 = [i[:len(term_states)] for i in [j for j in probs]]
    sub_matrix_2 = [i[len(term_states):] for i in [j for j in probs]]

    n = len(sub_matrix_2)
    identity = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                identity[j][i] = 1

    subtr_matrices = []
    for i, a in enumerate(identity):
        subtr_matrices.append(list(map(operator.sub, a, sub_matrix_2[i])))

    inverse = invert(subtr_matrices)
    final_matrix = multiplyMatrices(inverse, sub_matrix_1)

    dens = [i.denominator for i in final_matrix[0]]

    lcm = get_lcm_for(dens)

    term_states_probs = [(i.numerator / i.denominator) * lcm for i in final_matrix[0]]
    term_states_probs.append(lcm)
    term_states_probs = [int(i) for i in term_states_probs]
    return term_states_probs


def make_identity(r, c):
    """
    Make an identity matrix with dimensions rxc
    r - number of rows
    c - number of columns
    returns - list of lists corresponding to  the identity matrix
    """
    identity = []
    for i in range(0, r):
        row = []
        for j in range(0, c):
            elem = 0
            if i == j:
                elem = 1
            row.append(elem)
        identity.append(row)
    return identity


def check_for_all_zeros(X, i, j):
    """
    Check matrix X to see if only zeros exist at or below row i in column j
    X - a list of lists
    i - row index
    j - column index
    returns -
        zero_sum - the count of non zero entries
        first_non_zero - index of the first non value
    """
    non_zeros = []
    first_non_zero = -1
    for m in range(i, len(X)):
        non_zero = X[m][j] != 0
        non_zeros.append(non_zero)
        if first_non_zero == -1 and non_zero:
            first_non_zero = m
    zero_sum = sum(non_zeros)
    return zero_sum, first_non_zero


def swap_row(X, i, p):
    """
    Swap row i and row p in a list of lists
    X - list of lists
    i - row index
    p - row index
    returns- modified matrix
    """
    X[p], X[i] = X[i], X[p]
    return X


def invert(X):
    """
    Invert a matrix X according to gauss-jordan elimination
    In gauss-jordan elimination, we perform basic row operations to turn a matrix into
    row-echelon form.  If we concatenate an identity matrix to our input
    matrix during this process, we will turn the identity matrix into our inverse.
    X - input list of lists where each list is a matrix row
    output - inverse of X
    """
    # copy X to avoid altering input
    X = deepcopy(X)

    # Get dimensions of X
    rows = len(X)
    cols = len(X[0])

    # Get the identity matrix and append it to the right of X
    # This is done because our row operations will make the identity into the inverse
    identity = make_identity(rows, cols)
    for i in range(0, rows):
        X[i] += identity[i]

    i = 0
    for j in range(0, cols):
        # Check to see if there are any nonzero values below the current row in the current column
        zero_sum, first_non_zero = check_for_all_zeros(X, i, j)
        # If everything is zero, increment the columns
        if zero_sum == 0:
            if j == cols:
                return X
            raise Exception("Matrix is singular.")
        # If X[i][j] is 0, and there is a nonzero value below it, swap the two rows
        if first_non_zero != i:
            X = swap_row(X, i, first_non_zero)
        # Divide X[i] by X[i][j] to make X[i][j] equal 1
        X[i] = [m / X[i][j] for m in X[i]]

        # Rescale all other rows to make their values 0 below X[i][j]
        for q in range(0, rows):
            if q != i:
                scaled_row = [X[q][j] * m for m in X[i]]
                X[q] = [X[q][m] - scaled_row[m] for m in range(0, len(scaled_row))]
        # If either of these is true, we have iterated through the matrix, and are done
        if i == rows or j == cols:
            break
        i += 1

    # Get just the right hand matrix, which is now our inverse
    for i in range(0, rows):
        X[i] = X[i][cols:len(X[i])]

    return X


def multiplyMatrices(a, b):
    # confirm dimensions
    aRows = len(a)
    aCols = len(a[0])
    bRows = len(b)
    bCols = len(b[0])
    assert (aCols == bRows)  # belongs in a contract
    rows = aRows
    cols = bCols
    # create the result matrix c = a*b
    c = make2dList(rows, cols)
    # now find each value in turn in the result matrix
    for row in range(rows):
        for col in range(cols):
            dotProduct = Fraction(0, 1)
            for i in range(aCols):
                dotProduct += a[row][i] * b[i][col]
            c[row][col] = dotProduct
    return c


def make2dList(rows, cols):
    a = []
    for row in range(rows): a += [[0] * cols]
    return a


def lcm(a, b):
    if a > b:
        greater = a
    else:
        greater = b
    while True:
        if greater % a == 0 and greater % b == 0:
            lcm = greater
            break
        greater += 1
    return lcm


def get_lcm_for(your_list):
    return reduce(lambda x, y: lcm(x, y), your_list)


l = [
    [0, 2, 1, 0, 0],
    [0, 0, 0, 3, 4],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

x = answer(l)
print(x)
