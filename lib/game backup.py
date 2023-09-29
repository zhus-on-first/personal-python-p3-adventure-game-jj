# Manages state of game: choices between scenario, monster, character
# Methods for how game mechanics work

from models.player import Player
from models.character import Character
from data.default_characters import default_characters
from data.default_monsters import default_monsters
from data.default_scenarios import default_scenarios
import random
from texttable import Texttable
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
                break # Exit loop if successful
            except ValueError as e:
                print(e)
                continue
    
        # Create table and save player object to db
        self.player.create_table()
        self.player.save()

    def choose_character(self):
        
        # Display available characters
        # t = Texttable()
        # t.add_rows([['Name', 'Age'], ['Alice', 24], ['Bob', 19]])
        # print(t.draw())

        table = Texttable()
        for index, character in enumerate(default_characters):
            table.add_rows([
                ["Index", "Class", "Description", "HP", "MP", "Power"],
                [index, character['Class'], character['Description'], character['HP'], 
                 character['MP'], character['Power']]
])

        # Display formatted table
        print("Available characters:")
        print(table.draw())
                
        while True:
            # Set user"s character choice
            choice = input("Enter the number of the character you want: ")

            try:
                if choice.isdigit():
                    character_choice = default_characters[int(choice)]
                    self.character = Character(name=character_choice.get("Name", "Unknown"), 
                           character_class = character_choice.get("Class", "Unknown"),
                           character_description = character_choice.get("Description", "Unknown"),
                           xp = character_choice.get("XP", 0),
                           hp = character_choice.get("HP", 0),
                           mp = character_choice.get("MP", 0),
                           power = character_choice.get("Power", 0),
                           player_id = self.player.id)
                    break # Exit loop if successful
                # else: 
                #     print("Invalid choice. Please enter a digit corresponding to the character type you want.")
                    
            except ValueError as e:
                print(e)

        while True:
            try:
                # Set custom character name
                custom_name = input("Enter a name for your character: ")
                self.character.name = custom_name
                break # Exit loop if successful
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
        # Player"s turn
        # Monster"s turn
        # Victory or death!
        pass

    # def start_game(self, name, email, character_choice):
    #     pass

    # def save_game(self, player, current_scenario, current_monster):
    #     pass

    # def load_game(self, player_id):
    #     pass

    # def exit_game():
    #     print("Thanks for playing. See you next time!")
    #     exit()
