# legal_moves, is_win, is_draw
import unittest
from typing import List
from minimax import find_best_move
from connectfour import C4Board, C4Piece
from board import Move, Board


class C4BoardMinimaxTestCase(unittest.TestCase):
    def test_easy_position(self):
        element0: C4Board.Column = C4Board.Column()
        element0.push(C4Piece.E)

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

        test_board1: Board = C4Board(position, C4Piece.R)
        answer1: Move = find_best_move(test_board1, 3)
        self.assertEqual(answer1, 1)

    def test_block_position(self):
        element0: C4Board.Column = C4Board.Column()
        element0.push(C4Piece.E)

        element1: C4Board.Column = C4Board.Column()
        element1.push(C4Piece.R)
        element1.push(C4Piece.R)

        element2: C4Board.Column = C4Board.Column()
        element0.push(C4Piece.R)
        element0.push(C4Piece.R)

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
        self.assertEqual(answer2, 3)


if __name__ == "__main__":
    unittest.main()
