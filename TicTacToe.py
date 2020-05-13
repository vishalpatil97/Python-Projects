import random


def display_board(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-|-|-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-|-|-')
    print(board[1] + '|' + board[2] + '|' + board[3])


def player_input():
    # output = (player1 marker, player2 marker)

    marker = ' '

    while marker != 'X' and marker != 'O':
        marker = input("Player1: choose X or O: ").upper()

    if marker == 'X':
        return 'X', 'O'
    else:
        return 'O', 'X'


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    return ((mark == board[1] and mark == board[2] and mark == board[3]) or
            (mark == board[4] and mark == board[5] and mark == board[6]) or
            (mark == board[7] and mark == board[8] and mark == board[9]) or
            (mark == board[7] and mark == board[4] and mark == board[1]) or
            (mark == board[8] and mark == board[5] and mark == board[2]) or
            (mark == board[9] and mark == board[6] and mark == board[3]) or
            (mark == board[1] and mark == board[5] and mark == board[9]) or
            (mark == board[3] and mark == board[5] and mark == board[7]))


def space_check(board, position):
    return board[position] == ' '


def choose_first():
    r = random.randint(1, 2)

    if r == 1:
        return 'player1'
    else:
        return 'player2'


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    # Board is full
    return True


def player_choice(board):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input("Choose a position: (1-9) "))

    return position


def replay():
    ch = input("Do you Want to play again: Yes or No ")
    return ch == "Yes"


print("************WELCOME TO TIC TAC TOE************")

while True:
    # Play the game

    # Set Everything Up
    game_board = [' '] * 10
    player1_mark, player2_mark = player_input()
    turn = choose_first()
    print(turn + " will go first")

    play_game = input("Ready to play? y or n? ")
    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    # gamePlay

    while game_on:
        if turn == 'player1':
            # player one turn
            display_board(game_board)
            player1_pos = player_choice(game_board)  # player choosing position
            place_marker(game_board, player1_mark, player1_pos)  # placing the marker on board
            if win_check(game_board, player1_mark):  # win Check
                display_board(game_board)
                print('Player1 won the match')
                game_on = False
            elif full_board_check(game_board):  # Tie check
                display_board(game_board)
                print('Match tie!')
                game_on = False
            else:
                turn = 'player2'

        if turn == 'player2':
            # player two turn
            display_board(game_board)
            player2_pos = player_choice(game_board)
            place_marker(game_board, player2_mark, player2_pos)
            if win_check(game_board, player2_mark):
                display_board(game_board)
                print('Player2 won the match')
                game_on = False
            elif full_board_check(game_board):
                display_board(game_board)
                print('Match tie!')
                game_on = False
            else:
                turn = 'player1'

    if not replay():
        break
