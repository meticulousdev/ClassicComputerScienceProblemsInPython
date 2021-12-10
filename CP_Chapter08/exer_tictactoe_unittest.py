# legal_moves, is_win, is_draw
import unittest
from typing import List
from tictactoe import TTTPiece, TTTBoard
from board import Move, Board


class TTTMinimaxTestCase(unittest.TestCase):
    def test_illegal_moves(self):
        to_next_illegal_position: List[TTTPiece] = [TTTPiece.X, TTTPiece.E, TTTPiece.E,
                                                  TTTPiece.E, TTTPiece.E, TTTPiece.O,
                                                  TTTPiece.E, TTTPiece.X, TTTPiece.O]

        board: Board = TTTBoard(to_next_illegal_position)
        move: Move = Move(0) 
        answer1_1: bool = move in board.legal_moves
        self.assertEqual(answer1_1, False)

    def test_legal_moves(self):
        to_next_legal_position: List[TTTPiece] = [TTTPiece.X, TTTPiece.E, TTTPiece.E,
                                                  TTTPiece.E, TTTPiece.E, TTTPiece.O,
                                                  TTTPiece.E, TTTPiece.X, TTTPiece.O]

        board: Board = TTTBoard(to_next_legal_position)
        move: Move = Move(0) 
        answer1_2: bool = move in board.legal_moves
        self.assertEqual(answer1_2, False)

    def test_is_win(self):
        to_win_position: List[TTTPiece] = [TTTPiece.X, TTTPiece.O, TTTPiece.O,
                                           TTTPiece.X, TTTPiece.X, TTTPiece.O,
                                           TTTPiece.O, TTTPiece.X, TTTPiece.O]
        
        board: Board = TTTBoard(to_win_position) 
        answer2: bool = board.is_win
        self.assertEqual(answer2, True)

    def test_is_draw(self):
        to_draw_position: List[TTTPiece] = [TTTPiece.X, TTTPiece.O, TTTPiece.X,
                                            TTTPiece.X, TTTPiece.O, TTTPiece.O,
                                            TTTPiece.O, TTTPiece.X, TTTPiece.O]
        
        board: Board = TTTBoard(to_draw_position) 
        answer3: bool = board.is_draw
        self.assertEqual(answer3, True)


if __name__ == "__main__":
    unittest.main()
