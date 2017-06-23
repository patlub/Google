def answer(s):
    """
    Encoder/Decoder method
    """
    if not isinstance(s, str):
        raise TypeError('Argument should be of type String')

    # Dictionary to hold the Key
    key = {'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w', 'e': 'v', 'f': 'u',
           'g': 't', 'h': 's', 'i': 'r', 'j': 'q', 'k': 'p', 'l': 'o',
           'm': 'n', 'n': 'm', 'o': 'l', 'p': 'k','q': 'j', 'r': 'i',
           's': 'h', 't': 'g', 'u': 'f', 'v': 'e', 'w': 'd', 'x': 'c',
           'y': 'b', 'z': 'a'}

    dec_string = []
    for ch in s:
        letter = key.setdefault(ch, ch)
        dec_string.append(letter)
    return "".join(dec_string)


