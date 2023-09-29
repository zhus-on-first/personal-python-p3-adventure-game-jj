# Manages state of game: choices between scenario, monster, character
# Methods for how game mechanics work

from models.player import Player
from models.character import Character
from data.default_characters import default_characters
from data.default_monsters import default_monsters
from data.default_scenarios import default_scenarios
import random

class Game:
    def __init__(self, player, character):
        self.player = player
        self.character = character
        self.current_monster = None
        self.current_scenario = None

    def register_player(self):
        while True:
            print("Let's register your account first.")
            player_username = input("Enter your user name: ")
            player_email = input("Enter your email: ")

            try:
                # Initialize Player instance
                self.player = Player(player_username, player_email)
                break
            except ValueError as e:
                print(e)
                continue
    
        # Create table and save player object to db
        self.player.create_table()
        self.player.save()

    def choose_character(self):
        while True:
            # Display available characters
            print("Available characters:")
            for index, character in enumerate(default_characters):
                print(f"{index}. {character['Class']}")

            # Set user's character choice
            choice = input("Enter the number of the character you want: ")

            try:
                if choice.isdigit():
                    character_choice = default_characters[int(choice)]
                    self.character = Character(character_choice, self.player.id)
                    break
                else: 
                    print("Invalid choice. Please enter a digit corresponding to the character type you want.")
                    
            except ValueError as e:
                print(e)
        while True:
            try:
                # Set custom character name
                custom_name = input("Enter a name for your character: ")
                self.character.name = custom_name
                break
            except ValueError as e:
                print(e)
                continue

        # Save character type selection and custom name to db
        self.character.create_table()
        self.character.save()

    def random_encounter(self):
        # Generate a random scenario with random monster
        self.current_scenario = random.choice(default_scenarios)
        self.current_monster = random.choice(default_monsters)

    def battle(self):
        # Battle sequence
        # Player's turn
        # Monster's turn
        # Victory or death!
        pass

    def start_game(self, name, email, character_choice):
        pass

    def save_game(self, player, current_scenario, current_monster):
        pass

    def load_game(self, player_id):
        pass
    
    def view_stats(self):
        pass

    def exit_game():
        print(f"Thanks for playing {player.name}. See you next time!")
        exit()
