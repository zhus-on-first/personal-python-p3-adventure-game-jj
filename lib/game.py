# Manages state of game: interchoices between scenario, monster, character
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

    def register_player(self, name, email):
        self.player = Player(name, email)

    def choose_character(self, character_choice):
        self.character = Character(character_choice)

    def random_encounter(self):
        # Generate a random scenario with random monster
        self.current_scenario = random.choice(default_scenarios)
        self.current_monster = random.choice(default_monsters)

    def battle(self):
        # Battle sequence
        # Player's turn
        # Monster's turn
        #Victory or death!
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