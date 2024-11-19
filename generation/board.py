# attempt 2 to generate 


class ChessBoard:
    # we in a class

    board = []

    def __init__(self):
        self.board = [['.' for __ in range(8)] for _ in range(8)]
        return


    # standard: white == capital letter pieces
    def print_board(self):
        c = 8
        print()
        for row in self.board:
            print(c, '| ',end='')
            for sq in row:
                print(sq, end = ' ')
            
            print()
            c -= 1

        print('  + - - - - - - - -')
        print('    a b c d e f g h')
        print()
        return 

    def upd_sq(self, sq, piece):
        # sq is a string (e.g. 'a1', 'b3')
        
        # so a1 --> column a, row 1
        row = 8 - (ord(sq[1]) - ord('1') + 1)
        

        # a --> position 0 in the list
        column = ord(sq[0]) - ord('a')

        self.board[row][column] = piece
        return 

    
    def set_board(self, board_state):
        self.board = board_state
        return
    

    def set_board_to_fen(self, fen):
        parts = fen.split()
        
        # parts[0] -- actual board
        # parts[1] -- who's move? (w/b)
        # parts[2] -- castling?
        # parts[3] -- en passant target square (if exists)
        # parts[4] -- halfmove clock 


    



board = ChessBoard()
board.print_board()

board.upd_sq("a1", "N")
board.upd_sq("e4", "P")
board.upd_sq("f8", "b")
board.print_board()
