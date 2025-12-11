
import numpy as np
from settings import *

class Board:
    def __init__(self):
        self.grid = np.zeros((ROW_COUNT, COLUMN_COUNT))

    def drop_piece(self, row, col, piece):
        self.grid[row][col] = piece

    def is_valid_location(self, col):
        return self.grid[ROW_COUNT - 1][col] == 0

    def get_next_open_row(self, col):
        for r in range(ROW_COUNT):
            if self.grid[r][col] == 0:
                return r

    def get_valid_locations(self):
        valid_locations = []
        for col in range(COLUMN_COUNT):
            if self.is_valid_location(col):
                valid_locations.append(col)
        return valid_locations

    def check_win(self, piece):
       
        for c in range(COLUMN_COUNT - 3):
            for r in range(ROW_COUNT):
                if self.grid[r][c] == piece and self.grid[r][c+1] == piece and self.grid[r][c+2] == piece and self.grid[r][c+3] == piece:
                    return True

        
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT - 3):
                if self.grid[r][c] == piece and self.grid[r+1][c] == piece and self.grid[r+2][c] == piece and self.grid[r+3][c] == piece:
                    return True

      
        for c in range(COLUMN_COUNT - 3):
            for r in range(ROW_COUNT - 3):
                if self.grid[r][c] == piece and self.grid[r+1][c+1] == piece and self.grid[r+2][c+2] == piece and self.grid[r+3][c+3] == piece:
                    return True

       
        for c in range(COLUMN_COUNT - 3):
            for r in range(3, ROW_COUNT):
                if self.grid[r][c] == piece and self.grid[r-1][c+1] == piece and self.grid[r-2][c+2] == piece and self.grid[r-3][c+3] == piece:
                    return True
        return False
    
    def copy(self):
        new_board = Board()
        new_board.grid = self.grid.copy()
        return new_board