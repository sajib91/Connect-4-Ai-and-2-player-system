
import pygame
import sys
import math
import random
from settings import *
from board import Board
from ai import Connect4AI

class GameController:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SIZE)
        pygame.display.set_caption("Connect 4: Python Project")
        self.font = pygame.font.SysFont("monospace", 75)
        self.menu_font = pygame.font.SysFont("monospace", 40)
        
        self.board = Board()
        self.ai = Connect4AI()
        
        self.game_over = False
        self.turn = random.randint(PLAYER1, PLAYER2)
        self.game_mode = None # 

    def draw_board(self):
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):
                pygame.draw.rect(self.screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
                pygame.draw.circle(self.screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
        
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):
                if self.board.grid[r][c] == P1_PIECE:
                    pygame.draw.circle(self.screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), HEIGHT - int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
                elif self.board.grid[r][c] == P2_PIECE:
                    pygame.draw.circle(self.screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), HEIGHT - int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
        pygame.display.update()

    def show_menu(self):
        """Displays the selection menu to the user."""
        self.screen.fill(BLACK)
        title = self.font.render("CONNECT 4", 1, WHITE)
        option1 = self.menu_font.render("Press 1: Human vs AI", 1, YELLOW)
        option2 = self.menu_font.render("Press 2: Human vs Human", 1, RED)
        
        self.screen.blit(title, (WIDTH//2 - title.get_width()//2, 100))
        self.screen.blit(option1, (WIDTH//2 - option1.get_width()//2, 300))
        self.screen.blit(option2, (WIDTH//2 - option2.get_width()//2, 400))
        
        pygame.display.update()

        
        selected = False
        while not selected:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        self.game_mode = 'ai'
                        selected = True
                    if event.key == pygame.K_2:
                        self.game_mode = 'pvp'
                        selected = True

    def run(self):
        
        self.show_menu()
        
       
        self.draw_board()
        print(f"Mode: {self.game_mode.upper()} | First Turn: {'Player 1' if self.turn == PLAYER1 else 'Player 2/AI'}")
        
        while not self.game_over:
            
           
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.MOUSEMOTION:
                    pygame.draw.rect(self.screen, BLACK, (0, 0, WIDTH, SQUARESIZE))
                    posx = event.pos[0]
                    
                    if self.turn == PLAYER1:
                        pygame.draw.circle(self.screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)
                    elif self.turn == PLAYER2 and self.game_mode == 'pvp':
                        pygame.draw.circle(self.screen, YELLOW, (posx, int(SQUARESIZE/2)), RADIUS)
                        
                    pygame.display.update()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.rect(self.screen, BLACK, (0, 0, WIDTH, SQUARESIZE))
                    
                   
                    if self.turn == PLAYER1:
                        posx = event.pos[0]
                        col = int(math.floor(posx/SQUARESIZE))

                        if self.board.is_valid_location(col):
                            row = self.board.get_next_open_row(col)
                            self.board.drop_piece(row, col, P1_PIECE)

                            if self.board.check_win(P1_PIECE):
                                label = self.font.render("Player 1 Wins!!", 1, RED)
                                self.screen.blit(label, (40, 10))
                                self.game_over = True

                            self.turn = PLAYER2
                            self.draw_board()

                    
                    elif self.turn == PLAYER2 and self.game_mode == 'pvp':
                        posx = event.pos[0]
                        col = int(math.floor(posx/SQUARESIZE))

                        if self.board.is_valid_location(col):
                            row = self.board.get_next_open_row(col)
                            self.board.drop_piece(row, col, P2_PIECE)

                            if self.board.check_win(P2_PIECE):
                                label = self.font.render("Player 2 Wins!!", 1, YELLOW)
                                self.screen.blit(label, (40, 10))
                                self.game_over = True

                            self.turn = PLAYER1
                            self.draw_board()

            
            if self.game_mode == 'ai' and self.turn == AI_PLAYER and not self.game_over:
                
                col, score = self.ai.minimax(self.board, SEARCH_DEPTH, -math.inf, math.inf, True)

                if self.board.is_valid_location(col):
                    row = self.board.get_next_open_row(col)
                    self.board.drop_piece(row, col, P2_PIECE)

                    if self.board.check_win(P2_PIECE):
                        label = self.font.render("AI Wins!!", 1, YELLOW)
                        self.screen.blit(label, (40, 10))
                        self.game_over = True

                    self.draw_board()
                    self.turn = PLAYER1

        if self.game_over:
            pygame.time.wait(3000)

if __name__ == "__main__":
    game = GameController()
    game.run()