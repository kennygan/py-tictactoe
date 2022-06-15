board = [['X', ' ', 'O'],
         ['X', 'O', 'X'],
         ['O', 'X', 'X']]

position_dict = {'7': [0, 0], '8': [0, 1], '9': [0, 2],
                 '4': [1, 0], '5': [1, 1], '6': [1, 2],
                 '1': [2, 0], '2': [2, 1], '3': [2, 2]}


def display_reset():
    for value in position_dict.values():
        board[value[0]][value[1]] = ' '


def display_init():
    for key, value in position_dict.items():
        board[value[0]][value[1]] = key
    print("This is the board layout, positions are same as your number-pad.")
    display_board()


def player_init():
    marker = ' '
    while marker != "X" and marker != "O":
        marker = input("Player 1, choose your marker, X or O? :")
    player1_marker = marker
    if player1_marker == 'X':
        player2_marker = 'O'
    else:
        player2_marker = 'X'

    print("Player 1, you have chosen: " + player1_marker)
    print("Player 2, you are assigned with:" + player2_marker)
    return player1_marker, player2_marker


def player_input(player, marker):
    is_position_occupied = True
    while is_position_occupied is True:
        board_position = input(player + ", Enter your position:")
        x, y = position_dict[board_position]
        if board[x][y] == 'X' or board[x][y] == 'O':
            print("The position entered is occupied. Enter again.")
            is_position_occupied = True
        else:
            is_position_occupied = False

    board[x][y] = marker


def display_board():
    print("<<<<<<<<")
    for row in board:
        print(row[0] + '|' + row[1] + '|' + row[2])
        print("-|-|-")
    print(">>>>>>>>\n")


def verify_winner(marker):
    if ((board[0][0] == board[0][1] == board[0][2] == marker) or #first row
            (board[1][0] == board[1][1] == board[1][2] == marker) or #second row
            (board[2][0] == board[2][1] == board[2][2] == marker) or #third row
            (board[0][0] == board[1][0] == board[2][0] == marker) or #first column
            (board[0][1] == board[1][1] == board[2][1] == marker) or #second column
            (board[0][2] == board[1][2] == board[2][2] == marker) or #third column
            (board[0][0] == board[1][1] == board[2][2] == marker) or #diagonal
            (board[0][2] == board[1][1] == board[2][0] == marker)): #diagonal
        return True
    else:
        return False


def check_board_full():
    for row in board:
        for i in range(3):
            if row[i] == ' ':
                return False
    return True


if __name__ == '__main__':
    display_init()

    player1_marker, player2_marker = player_init()
    display_reset()

    is_game_over = False
    player_turn = "Player 1"
    while is_game_over is False:
        if player_turn == "Player 1":
            player_input(player_turn, player1_marker)
            if verify_winner(player1_marker) is True:
                print(player_turn + ' wins!')
                is_game_over = True
            else:
                if check_board_full() is True:
                    print('Game draw!')
                    is_game_over = True
                else:
                    player_turn = "Player 2"
            display_board()
        else:
            player_input(player_turn, player2_marker)
            if verify_winner(player2_marker) is True:
                print(player_turn + ' wins!')
                is_game_over = True
            else:
                if check_board_full() is True:
                    print('Game draw!')
                    is_game_over = True
                else:
                    player_turn = "Player 1"
            display_board()