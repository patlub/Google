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

    deltas = [(-2, -1), (-2, 1), (2, -1), (2, 1),
              (-1, -2), (-1, 2), (1, -2), (1, 2)]

    moves = [(i[0] + src[0], i[1] + src[1]) for i in deltas]
    if dest in moves:
        print(moves)
        return 1


    s_moves = []
    for move in moves:
        s_moves = [(i[0] + move[0], i[1] + move[1]) for i in deltas]
        if dest in s_moves:
            print(s_moves)
            return 2

    t_moves = []
    for move in s_moves:
        t_moves = [(i[0] + move[0], i[1] + move[1]) for i in deltas]
        if dest in t_moves:
            print(t_moves)
            return 3

    for move in t_moves:
        f_moves = [(i[0] + move[0], i[1] + move[1]) for i in deltas]
        if dest in f_moves:
            print(f_moves)
            return 4


print(answer((3, 2), (4, 4)))
