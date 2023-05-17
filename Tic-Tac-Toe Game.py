import random

# Tic Tac Toe

# Create the board
board = [' ' for _ in range(9)]

# Function to print the board
def print_board():
    print('-------------')
    for i in range(3):
        print('|', board[i * 3], '|', board[i * 3 + 1], '|', board[i * 3 + 2], '|')
        print('-------------')

# Function to check if there is a winner
def check_winner(player):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] == player:
            return True
    # Check columns
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] == player:
            return True
    # Check diagonals
    if board[0] == board[4] == board[8] == player or board[2] == board[4] == board[6] == player:
        return True
    return False

# Function for the player's move
def player_move():
    while True:
        position = int(input('Choose a position (1-9): ')) - 1
        if board[position] == ' ':
            board[position] = 'X'
            break
        else:
            print('Invalid move. Try again.')

# Function for the computer's move
def computer_move():
    # Check for winning move
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            if check_winner('O'):
                return
            else:
                board[i] = ' '

    # Check for player's winning move and block
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            if check_winner('X'):
                board[i] = 'O'
                return
            else:
                board[i] = ' '

    # Choose a random move
    while True:
        position = random.randint(0, 8)
        if board[position] == ' ':
            board[position] = 'O'
            return

# Function to play the game
def play_game():
    current_player = 'X'
    while True:
        print_board()

        if current_player == 'X':
            player_move()
        else:
            computer_move()

        if check_winner(current_player):
            print_board()
            if current_player == 'X':
                print('You win!')
            else:
                print('Computer wins!')
            break
        elif ' ' not in board:
            print_board()
            print("It's a tie!")
            break
        else:
            current_player = 'O' if current_player == 'X' else 'X'

# Start the game
play_game()
