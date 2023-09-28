# User interactions: the UI of it all
# Initializes Player and Game
# Main game loop

from models.player import Player
from models.character import Character
from game import Game

def main():
    print("Welcome to the Choose-Your-Adventure game!")
    
    player_name = input("Enter your name: ")
    player_email = input("Enter your email: ")

    # Get player's character choice
    character_choice = input("Choose your character type")

    # Initialize game with player and pass onto Game
    game = Game()
    
    game.start_game(player_name, player_email, character_choice)

    # Main game loop
    while True:
        print_main_menu()
        
        choice = input(f"Welcome {player_name}. What would you like to do?")
        
        if choice == "1":
            # start new game session
            game.start_game()
        elif choice == "2":
            # load previous game
            game.load_game()
        elif choice == "3":
            # view character stats belonging to specific player
            game.view_stats()
        elif choice == "5":
            pass
        elif choice == "???":
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
