## generate a weird position that is technically reachable

import random
'''
flow:
- generate pawn locations
- check to make sure no pieces are "locked in"
- generate all the other pieces 
(todo) -- make sure the king is not in check
'''


board = [['.' for __ in range(8)] for _ in range(8)]
piece_locations = set([])

def format(board):
    print()
    for row in board:
        for item in row:
            print(item, end=' ')
        
        print()
    print()
    return


def update(board, square, value):
    # square (e.g. a1)

    to_parse_rank = square[1]
    to_parse_file = square[0]

    actual_rank = int(to_parse_rank) - 1 # rank 1 = 0, etc.
    actual_file = ord(to_parse_file) - ord('a') # a = 0, b = 1, etc.


    board[7 - actual_rank][actual_file] = value # indices start at 0
    return



# generate pawns
for file in range(8):
    # file = 0 --> a
    # file = 1 --> b
    # file = 7 --> h
    # generate white pawn position then black pawn position
    
    # random.randint(1, 2) ==> 1, 2

    w_pawn_rank = -1
    b_pawn_rank = -1

    if random.randint(0, 1):
        w_pawn_rank = random.randint(2, 6) 
        b_pawn_rank = random.randint(w_pawn_rank + 1, 7)
    else:
        b_pawn_rank = random.randint(3, 7)
        w_pawn_rank = random.randint(2, b_pawn_rank - 1)

    piece_locations.add(chr(ord('a') + file)+str(w_pawn_rank))
    piece_locations.add(chr(ord('a') + file)+str(b_pawn_rank)) # do stuff

    update(board, chr(ord('a') + file)+str(w_pawn_rank), 'x')
    update(board, chr(ord('a') + file)+str(b_pawn_rank), 'o')

format(board)

# generate pieces
# gotta validate the king checker -- leave him out of check

# just keep on generate king positions that are
b_king_pos = ".."




# for simplicity generate white king before black king
