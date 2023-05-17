from typing import List
from minimax import find_best_move
from connectfour import C4Board, C4Piece
from board import Move, Board


if __name__ == "__main__":
    element0: C4Board.Column = C4Board.Column()
    element0.push(C4Piece.R)

    element1: C4Board.Column = C4Board.Column()
    element1.push(C4Piece.R)
    element1.push(C4Piece.R)
    element1.push(C4Piece.R)

    element2: C4Board.Column = C4Board.Column()
    element2.push(C4Piece.E)

    element3: C4Board.Column = C4Board.Column()
    element3.push(C4Piece.B)
    element3.push(C4Piece.B)
    element3.push(C4Piece.B)

    element4: C4Board.Column = C4Board.Column()
    element4.push(C4Piece.B)

    element5: C4Board.Column = C4Board.Column()
    element5.push(C4Piece.E)

    element6: C4Board.Column = C4Board.Column()
    element6.push(C4Piece.E)

    position: List[C4Board.Column] = [element0, element1, element2, element3, element4, element5, element6]

    test_board2: Board = C4Board(position, C4Piece.R)
    answer2: Move = find_best_move(test_board2, 3)
    print(test_board2)
    print(answer2)
