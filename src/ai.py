
import math
import random
from settings import *

class Connect4AI:
    def __init__(self):
        pass

    def evaluate_window(self, window, piece):
        score = 0
        opp_piece = P1_PIECE if piece == P2_PIECE else P2_PIECE

        if window.count(piece) == 4:
            score += 100
        elif window.count(piece) == 3 and window.count(EMPTY) == 1:
            score += 5
        elif window.count(piece) == 2 and window.count(EMPTY) == 2:
            score += 2

        if window.count(opp_piece) == 3 and window.count(EMPTY) == 1:
            score -= 4

        return score

    def score_position(self, board_obj, piece):
        score = 0
        grid = board_obj.grid
        center_array = [int(i) for i in list(grid[:, COLUMN_COUNT // 2])]
        center_count = center_array.count(piece)
        score += center_count * 3

        for r in range(ROW_COUNT):
            row_array = [int(i) for i in list(grid[r, :])]
            for c in range(COLUMN_COUNT - 3):
                window = row_array[c:c + WINDOW_LENGTH]
                score += self.evaluate_window(window, piece)

        for c in range(COLUMN_COUNT):
            col_array = [int(i) for i in list(grid[:, c])]
            for r in range(ROW_COUNT - 3):
                window = col_array[r:r + WINDOW_LENGTH]
                score += self.evaluate_window(window, piece)

        for r in range(ROW_COUNT - 3):
            for c in range(COLUMN_COUNT - 3):
                window = [grid[r + i][c + i] for i in range(WINDOW_LENGTH)]
                score += self.evaluate_window(window, piece)

        for r in range(ROW_COUNT - 3):
            for c in range(COLUMN_COUNT - 3):
                window = [grid[r + 3 - i][c + i] for i in range(WINDOW_LENGTH)]
                score += self.evaluate_window(window, piece)

        return score

    def is_terminal_node(self, board_obj):
        return board_obj.check_win(P1_PIECE) or \
               board_obj.check_win(P2_PIECE) or \
               len(board_obj.get_valid_locations()) == 0

    def minimax(self, board_obj, depth, alpha, beta, maximizingPlayer):
        valid_locations = board_obj.get_valid_locations()
        is_terminal = self.is_terminal_node(board_obj)

        if depth == 0 or is_terminal:
            if is_terminal:
                if board_obj.check_win(P2_PIECE):
                    return (None, 100000000000000)
                elif board_obj.check_win(P1_PIECE):
                    return (None, -10000000000000)
                else: 
                    return (None, 0)
            else:
                return (None, self.score_position(board_obj, P2_PIECE))

        if maximizingPlayer:
            value = -math.inf
            column = random.choice(valid_locations)
            for col in valid_locations:
                row = board_obj.get_next_open_row(col)
                b_copy = board_obj.copy()
                b_copy.drop_piece(row, col, P2_PIECE)
                new_score = self.minimax(b_copy, depth - 1, alpha, beta, False)[1]
                if new_score > value:
                    value = new_score
                    column = col
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return column, value

        else: 
            value = math.inf
            column = random.choice(valid_locations)
            for col in valid_locations:
                row = board_obj.get_next_open_row(col)
                b_copy = board_obj.copy()
                b_copy.drop_piece(row, col, P1_PIECE)
                new_score = self.minimax(b_copy, depth - 1, alpha, beta, True)[1]
                if new_score < value:
                    value = new_score
                    column = col
                beta = min(beta, value)
                if alpha >= beta:
                    break
            return column, value