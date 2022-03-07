from game import play_game

if __name__ == '__main__':
    play_game()

    play_again = input("The game has end, do you want to play again? Type Yes / No: ")
    if play_again == "Yes":
        play_game()
    else:
        print("Thanks for playing")