import pygame
import numpy as np

######### 1 is RED ########### 2 is YELLOW #######

pygame.init()

#Screen
screen = pygame.display.set_mode((700,680))
screen.fill("grey")
pygame.display.set_caption("Connect 4")
game_icon = pygame.image.load("Connect4_logo.png")
pygame.display.set_icon(game_icon)

#Board
board_rows = 6
board_cols = 7
board = np.zeros((board_rows,board_cols))
board_image = pygame.image.load("board_image.png")


def mark(row, cols,player):
    board[row][cols] = player

def move_available(row,cols):
    return board[row][cols] == 0

def get_available_row(col):
    for i in range(5,-1,-1):
        if board[i][col] == 0:
            return i

def get_available_col(col):
    return board[0][col] == 0

def check_winner(board, piece):
    for row in range(board_rows-3):
        for col in range(board_cols):
            if board[row][col]==piece and board[row+1][col]==piece and board[row+2][col] == piece and board[row+3][col]==piece:
                    return piece

    for row in range(board_rows):
        for col in range(board_cols-3):
            if board[row][col]==piece and board[row][col+1]==piece and board[row][col+2] == piece and board[row][col+3]==piece:
                return piece

    for row in range(board_rows-3):
        for col in range(board_cols-3):
            if board[row][col]==piece and board[row+1][col+1]==piece and board[row+2][col+2] == piece and board[row+3][col+3]==piece:
                return piece

    for row in range(3,board_rows):
        for col in range(board_cols-3):
            if board[row][col]==piece and board[row-1][col+1]==piece and board[row-2][col+2] == piece and board[row-3][col+3]==piece:
                return piece
    return False


win_font = pygame.font.SysFont("arial", 90, True,False)
yellow_win_txt = win_font.render("Yellow Wins", True, "Yellow")
red_win_txt = win_font.render("Red Wins", True, "Red")
draw_txt = win_font.render("Draw", True, "Black")


game_active = True

red_turn = True
red_piece = pygame.image.load("red_piece.png")
yellow_piece = pygame.image.load("yellow_piece.png")


running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if not game_active:

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    screen.fill("grey")
                    screen.blit(board_image, (0, 80))
                    board.fill(0)

                    game_active = True
        if game_active:

            if check_winner(board,1) == False:
                if check_winner(board,2) == False:
                    if board[0][0]>0 and board[0][1]>0 and board[0][2]>0 and board[0][3]>0 and board[0][4]> 0 and board[0][5]>0 and board[0][6]>0:
                        screen.blit(draw_txt, (170,-10))
                        game_active=False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] <= 660 and event.pos[1] <= 690:
                    mouse_x = event.pos[0]
                    mouse_y = event.pos[1]


                    row_pressed = int(mouse_y // 118)
                    cols_pressed = int(mouse_x // 95)

                    if get_available_col(cols_pressed):

                        row = get_available_row(cols_pressed)
                        if red_turn:
                            mark(row, cols_pressed, 1)
                            screen.blit(red_piece, (int(cols_pressed * 100+12), int(row * 100+80)))
                            red_turn = False
                            if check_winner(board, 1):
                                screen.blit(red_win_txt, (170,-10))
                                game_active = False



                        else:
                            mark(row, cols_pressed, 2)
                            screen.blit(yellow_piece, (int(cols_pressed * 100+12), int(row * 100+80)))
                            red_turn = True
                            if check_winner(board, 2):
                                screen.blit(yellow_win_txt, (150,-10))

                                game_active= False
        screen.blit(board_image, (0, 80))








    pygame.display.update()
