# User interactions: the UI of it all
# Initializes Player and Game
# Main game loop

from game import Game
from models.character import Character
from models.player import Player

def main():

    # Main game loop
    while True:
        print("*" * 50)
        print("Welcome to Choose-Your-Adventure. What would you like to do?")
        print_main_menu()
        print("Enter your choice >>")
        
        choice = input()
        
        try:
            if choice == "1":
                print("-" * 50)
                # Start new game session. Initialize game with player and pass onto Game.
                game = Game(None, None)
                game.register_player()
                game.choose_character()
                game.start_game()
                print("Enter your choice >>")
                print("-" * 50)
                continue

            elif choice == "2":
                print("-" * 50)
                # load previous game
                game.load_game()
                print("-" * 50)
                continue

            elif choice == "3":
                print("-" * 50)
                # view character stats belonging to specific player
                view_db_stats()
                print("-" * 50)
                continue

            elif choice == "4":
                game.exit_game()
            else:
                print("Invalid choice selection. Please try again.")
                continue

        except Exception as e:
            print(f"There was an error: {e}")
            print("Returning to main menu...")
            continue


def print_main_menu():
    print("1. Start New Game")
    print("2. Load Previous Game")
    print("3. View Your Characters' Stats")
    print("4. Exit")

def view_db_stats():
    # Access all characters
    characters = Character.get_all()

    # Print stats
    for character in characters:
        print(character.__dict__)
        print(f"\nCreated by {Player.find_by_id(character.player_id).username}")
        print(f"Name: {character.name}")
        print(f"Class: {character.character_class}")
        print(f"Description: {character.character_description}")
        print(f"XP: {character.xp}")
        print(f"HP: {character.hp}")
        print(f"MP: {character.mp}")
        print(f"Power: {character.power}")

if __name__ == "__main__":
    main()
