from minimax import find_best_move
from tictactoe import TTTBoard, TTTPiece
from board import Move, Board
from connectfour import C4Board, C4Piece

import sys
from typing import List, Optional


class GameAI:
    def __init__(self, game: int):
        self.board_list: List[Board] = [TTTBoard(), C4Board()]
        self.game_list: List[Optional] = [self.tictactoe_ai, self.connectfour_ai]
        self.messages: List[str] = ["이동할 위치를 입력하세요 (0-8): ", "이동할 열 위치를 입력하세요 (0-6): "]

        self.board: Board = self.board_list[game - 1]
        self.find_best_move = self.game_list[game - 1]

    def connectfour_ai(self) -> Move:
        connectfour_computer_move: Move = find_best_move(self.board, 3)
        return connectfour_computer_move

    def tictactoe_ai(self) -> Move:
        tictactoe_computer_move: Move = find_best_move(self.board)
        return tictactoe_computer_move

    def get_player_move(self, game: int) -> Move:
        player_move: Move = Move(-1)
        while player_move not in self.board.legal_moves:
            play: int = int(input(self.messages[game - 1]))
            player_move = Move(play)
        return player_move


if __name__ == "__main__":
    while True:
        print("1. Tic tac toe")
        print("2. Connect four")
        print("3. Exit")
        game: int = int(input("게임을 선택하세요: "))

        if game == 3:
            sys.exit()
        elif 1 > game or game > 3:
            print("1~3 사이의 숫자를 입력해주세요.")
        else:
            break

    game_ai: GameAI = GameAI(game)
    while True:
        human_move: Move = game_ai.get_player_move(game)
        game_ai.board = game_ai.board.move(human_move)
        if game_ai.board.is_win:
            print("당신이 이겼습니다!")
            break
        elif game_ai.board.is_draw:
            print("비겼습니다!")
            break

        computer_move: Move = game_ai.find_best_move()
        print(f"컴퓨터가 {computer_move}(으)로 이동했습니다.")
        game_ai.board = game_ai.board.move(computer_move)
        print(game_ai.board)
        if game_ai.board.is_win:
            print("컴퓨터가 이겼습니다!")
            break
        elif game_ai.board.is_draw:
            print("비겼습니다!")
            break
