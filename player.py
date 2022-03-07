from typing import List


def continue_game(board) -> bool:

    for i in range(3):
        # is there a win in each row?
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != 0:
            return False
        # is there a win in each column?
        elif board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != 0:
            return False

    return True

def change_player(player_number):
    if player_number == 1:
        new_player_number = 2
    elif player_number == 2:
        new_player_number = 1
    else:
        new_player_number = None
    return new_player_number

def play_move(board: List[List], player_number):
    row = int(input("Play position row: "))
    column = int(input("Play position column: "))
    if board[row][column] == 0:
        board[row][column] = player_number
        continue_to_next_move = continue_game(board)

        return board, continue_to_next_move
    else:
        print("Position is already taken, pick another one")
        play_move(board, player_number)