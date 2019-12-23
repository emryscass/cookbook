import random

# Tic Tac Toe Board
board = [

                        [' ', '|', ' ', '|',' '],
                        [' ', '|', ' ', '|',' '],
                        [' ', '|', ' ', '|',' ']

                        ]

# Display board
def display_board(board):
        for pos in board:
                print('\t'*2, pos, ' ', '\n', '\t'*2, '-'*6, '|', '-'*7, '|', '-'*6)


# Check for winner
def winner(board):
        if board[0].count('X') == 3 or board[0].count('O') == 3 or board[1].count('X') == 3 or board[1].count('O') == 3 or board[2].count('X') == 3 or board[2].count('O') == 3:
                win = 'Winner'
                return win
        elif board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X' or board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O':
                win = 'Winner'
                return win
        elif board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X' or board[0][2] == 'O' and board[1][2] == 'O' and board[2][2] == 'O':
                win = 'Winner'
                return win
        elif board[0][4] == 'X' and board[1][4] == 'X' and board[2][4] == 'X' or board[0][4] == 'O' and board[1][4] == 'O' and board[2][4] == 'O':
                win = 'Winner'
                return win
        elif board[0][0] == 'X' and board[1][2] == 'X' and board[2][4] == 'X' or board[0][0] == 'O' and board[1][2] == 'O' and board[2][4] == 'O':
                win = 'Winner'
                return win
        elif board[0][4] == 'X' and board[1][2] == 'X' and board[2][0] == 'X' or board[0][4] == 'O' and board[1][2] == 'O' and board[2][0] == 'O':
                win = 'Winner'
                return win


# Update Board
def update_board(board, row, column, player_turn):
        if player_turn.lower() == 'x':
                board[row][column] = 'X'
                for pos in board:
                        print('\t'*2, pos, ' ', '\n', '\t'*2, '-'*6, '|', '-'*7, '|', '-'*6)

        elif player_turn.lower() == 'o':
                board[row][column] = 'O'
                for pos in board:
                        print('\t'*2, pos, ' ', '\n', '\t'*2, '-'*6, '|', '-'*7, '|', '-'*6)


positions = [(0, 0), (0, 2), (0, 4), (1, 0), (1, 2), (1, 4), (2, 0), (2, 2), (2, 4)]


print('='*14, 'Tic Tac Toe', '='*14)
print('\n')
display_board(board)

print('\n')

print('Available moves')

for x in positions:
        print(x)

print('\n')


for turn in range(0, 9):
        if turn % 2 == 0:
                while True:
                        player_turn = 'X'
                        print('X\'s turn')
                        row = int(input('What row? '))
                        column = int(input('What column? '))
                        if ((row, column)) in positions:
                                positions.remove((row, column))
                                print(f'Remaining positions: {positions}')
                                print('\n')
                                update_board(board, row, column, player_turn)
                                check = winner(board)
                                if check == 'Winner':
                                        print(check)
                                        break
                                break
                        else:
                                print('\n')
                                print(f'Sorry, that range has either already been used or isnt within the grid. Your options are: {positions}')
                                print('\n')

        else:
                player_turn = 'O'
                print('O\'s turn')
                computer = random.choice(positions)
                row = computer[0]
                column = computer[1]

                positions.remove(computer)
                print(f'Remaining positions: {positions}')
                print('\n')
                update_board(board, row, column, player_turn)
                check = winner(board)
                if check == 'Winner':
                        print(check)
                        break
