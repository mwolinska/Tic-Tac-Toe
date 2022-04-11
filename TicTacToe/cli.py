import os


def one_player_game():
    os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "True"
    from TicTacToe.tic_tac_toe import single_player_game_main
    single_player_game_main()

def two_player_game():
    from TicTacToe.tic_tac_toe import two_player_game_main
    two_player_game_main()
