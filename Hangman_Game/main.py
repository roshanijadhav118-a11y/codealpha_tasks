from game import play_game


def main():

    while True:

        play_game()

        choice = input("\nDo you want to play again? (y/n): ").lower().strip()

        if choice != "y":
            print("\nThank you for playing Hangman!")
            break


if __name__ == "__main__":
    main()