# User interactions: the UI of it all
# Initializes Player and Game
# Main game loop

from game import Game

def main():
    #Initialize game to prevent error if choose 2-4.
    game = None

    # Main game loop
    while True:
        print("Welcome to Choose-Your-Adventure. What would you like to do?")
        print_main_menu()
        
        choice = input()
        
        if choice == "1":
            # Start new game session. Initialize game with player and pass onto Game.
            game = Game(None, None)
            game.register_player()
            game.choose_character()
            game.start_game()

        elif choice == "2":
            # load previous game
            game.load_game()

        elif choice == "3":
            # view character stats belonging to specific player
            game.view_stats()

        elif choice == "4":
            game.exit_game()
        else:
            print("Invalid option. Please try again.")


def print_main_menu():
    print("1. Start New Game")
    print("2. Load Previous Game")
    print("3. View Stats")
    print("4. Exit")

if __name__ == "__main__":
    main()
