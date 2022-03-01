from __future__ import annotations
from board import Piece, Board, Move


# The maximizing player aims to find the move that will lead to maximal gains.
# However, the maximizing player must account for moves by the minimizing player.
# After each attempt to maximize the gains of the maximizing player,
# minimax is called recursively to find the opponent’s reply that minimizes the maximizing player’s gains.
# This continues back and forth (maximizing, minimizing, maximizing, and so on)
# until a base case in the recursive function is reached.
# The base case is a terminal position (a win or a draw) or a maximal search depth.
def minimax(board: Board, maximizing: bool, original_player: Piece, max_depth: int = 8) -> float:
    if board.is_win or board.is_draw or max_depth == 0:
        return board.evaluate(original_player)

    if maximizing:
        best_eval: float = float("-inf")
        for move in board.legal_moves:
            result: float = minimax(board.move(move), False, original_player, max_depth - 1)
            best_eval = max(result, best_eval)
        return best_eval
    else:
        worst_eval: float = float("inf")
        for move in board.legal_moves:
            result = minimax(board.move(move), True, original_player, max_depth - 1)
            worst_eval = min(result, worst_eval)
        return worst_eval
# end of minimax


def find_best_move(board: Board, max_depth: int = 8) -> Move:
    best_eval: float = float("-inf")
    best_move: Move = Move(-1)
    for move in board.legal_moves:
        # result: float = minimax(board.move(move), False, board.turn, max_depth)
        result: float = alphabeta(board.move(move), False, board.turn, max_depth)
        if result > best_eval:
            best_eval = result
            best_move = move
    return best_move
# end of find_best_move


def alphabeta(board: Board, maximizing: bool, original_player: Piece,
              max_depth: int = 8, alpha: float = float("-inf"), beta: float = float("inf")) -> float:
    # alpha: maximizing
    # beta: minimizing
    if board.is_win or board.is_draw or max_depth == 0:
        return board.evaluate(original_player)

    if maximizing:
        for move in board.legal_moves:
            result: float = alphabeta(board.move(move), False, original_player,
                                      max_depth - 1, alpha, beta)
            alpha = max(result, alpha)
            if beta <= alpha:
                break
        return alpha
    else:  # minimizing
        for move in board.legal_moves:
            result = alphabeta(board.move(move), True, original_player,
                               max_depth - 1, alpha, beta)
            beta = min(result, beta)
            if beta <= alpha:
                break
        return beta
