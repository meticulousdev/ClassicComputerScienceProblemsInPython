from minimax import find_best_move
from connectfour import C4Board, C4Piece
from board import Move, Board
from random import randint

# board: Board = C4Board()


if __name__ == "__main__":

    total_game: int = 10
    black_win: int = 0
    red_win: int = 0
    draw: int = 0

    for i in range(0, total_game):
        print(f"판: {i+1}")
        board: Board = C4Board()
        first_turn = 1

        while True:
            if first_turn == 1:
                black_move: Move = Move(randint(0, 6))
                first_turn = 0
            else:
                black_move = find_best_move(board, 3)
            print(f"블랙이 {black_move}열을 선택했습니다.")
            board = board.move(black_move)

            if board.is_win:
                print("블랙이 이겼습니다!")
                black_win += 1
                break
            elif board.is_draw:
                print("비겼습니다!")
                draw += 1
                break

            red_move: Move = find_best_move(board, 3)
            print(f"레드가 {red_move}열을 선택했습니다.")
            board = board.move(red_move)
            # print(board)

            if board.is_win:
                print("레드가 이겼습니다!")
                red_win += 1
                break
            elif board.is_draw:
                print("비겼습니다!")
                draw += 1
                break
        print(board)
        print()

    print(f"블랙의 승률: {black_win/total_game}")
    print(f"레드의 승률: {red_win/total_game}")
