from minimax import find_best_move
from connectfour import C4Board, C4Piece
from board import Move, Board

board: Board = C4Board()


def get_player_move() -> Move:
    player_move: Move = Move(-1)
    while player_move not in board.legal_moves:
        play: int = int(input("이동할 열 위치를 입력하세요 (0-6): "))
        player_move = Move(play)
    return player_move


if __name__ == "__main__":
    while True:
        human_move: Move = get_player_move()
        board = board.move(human_move)

        if board.is_win:
            print("당신이 이겼습니다!")
            break
        elif board.is_draw:
            print("비겼습니다!")
            break

        computer_move: Move = find_best_move(board, 3)
        print(f"컴퓨터가 {computer_move}열을 선택했습니다.")
        board = board.move(computer_move)
        print(board)

        if board.is_win:
            print("컴퓨터가 이겼습니다!")
            break
        elif board.is_draw:
            print("비겼습니다!")
            break
