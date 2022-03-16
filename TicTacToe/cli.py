import TicTacToe

if __name__ == '__main__':
    my_game = TicTacToe.TicTacToe(
        number_of_human_players=1,
        number_of_random_players=1,
    )
    my_game.play_game()
