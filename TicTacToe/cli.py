import TicTacToe

def one_player_game():
    my_game = TicTacToe.TicTacToe(
        number_of_human_players=1,
        number_of_random_players=1,
    )
    my_game.play_game()

def two_player_game():
    my_game = TicTacToe.TicTacToe(
        number_of_human_players=2,
    )
    my_game.play_game()
