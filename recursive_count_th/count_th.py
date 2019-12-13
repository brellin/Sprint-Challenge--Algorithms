'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def thith(piece, count=0):
    print(piece)

    # if length of "th" not possible, return current count
    if len(piece) < 2:
        return count

    # if first two letters of current piece of word are "th", increase the count
    elif piece[:2] == 'th':
        count += 1

    # create substring with one less character for next iteration of thith (Mike Tyson) function
    return thith(piece[1:], count)


def count_th(word):
    return thith(word)
