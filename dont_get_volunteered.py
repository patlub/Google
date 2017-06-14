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
    """
    Minimum knight moves for Chess
    
    Arguments:
        src:  Initial knight position
        dest: Final knight position
        
    Raises:
        TypeError: For non-int args
    
    Returns:
        int: Number of knight moves
    """

    if not isinstance(src, int) or not isinstance(dest, int):
        raise TypeError('Both source and destination should be ints')

    elif not 0 <= src <= 63:
        return 'Source argument out of valid range(0 - 63)'

    elif not 0 <= dest <= 63:
        return 'Destination argument out of valid range(0 - 63)'

    if src == dest:
        return 0

    # Convert args to points
    src = (src % 8, src // 8)
    dest = (dest % 8, dest // 8)

    # All Possible moves
    deltas = [(-2, -1), (-2, 1), (2, -1), (2, 1),
              (-1, -2), (-1, 2), (1, -2), (1, 2)]

    # All possible First moves
    moves = [(i[0] + src[0], i[1] + src[1]) for i in deltas]

    if dest in moves:
        return 1

    # Make all possible moves until the
    # destination is reached, otherwise
    # return 6, the maximium possible moves
    count = 1
    while count < 6:
        next_moves = []
        for move in moves:
            sub_moves = [(i[0] + move[0], i[1] + move[1]) for i in deltas]
            if dest in sub_moves:
                if count == 1:
                    return 2
                if count == 2:
                    return 3
                if count == 3:
                    return 4
                if count == 4:
                    return 5
            else:
                for sub_move in sub_moves:
                    next_moves.append(sub_move)

        moves = next_moves
        count += 1
    return 6
