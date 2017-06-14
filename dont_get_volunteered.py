"""
Don't Get Volunteered!
======================

To help yourself get to and from your bunk every day, write a function called
answer(src, dest) which takes in two parameters: the source square, on which
you start, and the destination square, which is where you need to land to 
solve the puzzle.  The function should return an integer representing the
smallest number of moves it will take for you to travel from the source
square to the destination square using a chess knight's moves (that is, two
squares in any direction immediately followed by one square perpendicular to
that direction, or vice versa, in an "L" shape).  Both the source and 
destination squares will be an integer between 0 and 63, inclusive, and are
numbered like the example chessboard below:
"""


def answer(src, dest):
    """Minimim knight moves for Chess"""

    if not isinstance(src, int) or not isinstance(dest, int):
        raise TypeError('Both source and destination should be ints')

    elif not 0 <= src <= 63:
        return 'Source argument out of valid range(0 - 63)'

    elif not 0 <= dest <= 63:
        return 'Destination argument out of valid range(0 - 63)'

    if src == dest:
        return 0

    src = (src % 8, src // 8)
    dest = (dest % 8, dest // 8)

    deltas = [(-2, -1), (-2, 1), (2, -1), (2, 1),
              (-1, -2), (-1, 2), (1, -2), (1, 2)]

    first_nodes = [(i[0] + src[0], i[1] + src[1]) for i in deltas]
    second_nodes = []
    third_nodes = []
    fourth_nodes = []

    if dest in first_nodes:
        return 1

    for node in first_nodes:
        sub_nodes = [(i[0] + node[0], i[1] + node[1]) for i in deltas]
        if dest in sub_nodes:
            return 2
        else:
            for sub_node in sub_nodes:
                second_nodes.append(sub_node)

    for node in second_nodes:
        sub_nodes = [(i[0] + node[0], i[1] + node[1]) for i in deltas]
        if dest in sub_nodes:
            return 3
        else:
            for sub_node in sub_nodes:
                third_nodes.append(sub_node)

    for node in third_nodes:
        sub_nodes = [(i[0] + node[0], i[1] + node[1]) for i in deltas]
        if dest in sub_nodes:
            return 4
        else:
            for sub_node in sub_nodes:
                fourth_nodes.append(sub_node)

    for node in fourth_nodes:
        sub_nodes = [(i[0] + node[0], i[1] + node[1]) for i in deltas]
        if dest in sub_nodes:
            return 5
    return 6


print(answer(0, 1))
