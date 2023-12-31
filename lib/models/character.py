from models.__init__ import CURSOR, CONN
from models.player import Player
import re

class Character:
    ALL = {}

    def __init__(self, name, character_class, character_description, xp, hp, mp, power, player_id, id=None):
        self.id = id
        self.name = name
        self.character_class = character_class
        self.character_description = character_description
        self.xp = xp
        self.hp = hp
        self.mp = mp
        self.power = power
        self.player_id = player_id

    def __repr__(self):
        player = Player.find_by_id(self.player_id)
        player_username = player.name if player else "None"
        return (
            f"<Character {self.id}: {self.name}, "
            f"Class: {self.character_class}, "
            f"Class: {self.character_description}, "
            f"XP: {self.xp}, "
            f"HP: {self.hp}, "
            f"MP: {self.mp}, "
            f"Power: {self.power}, "
            f"Owned by: {player_username} with id: {self.player_id}>"
            )

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        # TODO a unique name check
        if not isinstance(name, str):
            raise ValueError("The character name must be a string.")

        if not 3 <= len(name) <= 20:
            raise ValueError(
                "The character name's length must be between 3 and 20 characters."
                )

        if not name[0].isalpha():
            raise ValueError(
                "The character's name must start with an alphabetic letter."
                )

        if not re.match("^[a-zA-Z_]*$", name):
            raise ValueError(
                "The character's name can only contain letters and underscores."
                )

        # if not self.is_name_unique(name):
        #     raise ValueError("The character name must be unique.")

        self._name = name

    @property
    def character_class(self):
        return self._character_class
    
    @character_class.setter
    def character_class(self, character_class):
        if isinstance(character_class, str):
            self._character_class = character_class
        else:
            raise ValueError("Character class must be a string.")
        
    @property
    def character_description(self):
        return self._character_description
    
    @character_description.setter
    def character_description(self, character_description):
        if isinstance(character_description, str):
            self._character_description = character_description
        else:
            raise ValueError("Character description must be a string.")

    @property
    def xp(self):
        return self._xp

    @xp.setter
    def xp(self, xp):
        if isinstance(xp, int) and xp >= 0:
            self._xp = xp
        else:
            raise ValueError("XP must be a positive integer.")

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        if isinstance(hp, int) and hp >= 0:
            self._hp = hp
        else:
            raise ValueError("HP must be a positive integer.")

    @property
    def mp(self):
        return self._mp

    @mp.setter
    def mp(self, mp):
        if isinstance(mp, int) and mp >= 0:
            self._mp = mp
        else:
            raise ValueError("MP must be a positive integer.")
        
    @property
    def power(self):
        return self._power

    @power.setter
    def power(self, power):
        if isinstance(power, int) and power >= 0:
            self._power = power
        else:
            raise ValueError("Power must be a positive integer.")

    @property
    def player_id(self):
        return self._player_id

    @player_id.setter
    def player_id(self, player_id):
        if isinstance(player_id, int) and player_id >= 0:
            self._player_id = player_id
        else:
            raise ValueError("Player Id must be a positive integer.")
        
     # CRUD methods for Monster class below
    @classmethod
    def create_table(cls):
        # SQL command to create new Character table to persist attribute's character instance
        sql = """
            CREATE TABLE IF NOT EXISTS characters (
            id INTEGER PRIMARY KEY,
            name TEXT,
            character_class TEXT,
            character_description TEXT,
            xp INTEGER,
            hp INTEGER,
            mp INTEGER,
            power INTEGER,
            player_id INTEGER,
            FOREIGN KEY (player_id) REFERENCES players(id) ON DELETE CASCADE
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        # SQL command to drop character table that persists Character instances
        sql = """
            DROP TABLE IF EXISTS characters;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        # Save character instance to new database row
        sql = """
            INSERT INTO characters (name, character_class, character_description, xp, hp, mp, power, player_id)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """

        # Update object id attribute using the primary key value of new row
        CURSOR.execute(sql, (
            self.name, self.character_class, self.character_description, self.xp, self.hp, self.mp, self.power, self.player_id
            ))
        CONN.commit()

        # Save the object in local dictionary using table row's PK as dictionary key
        self.id = CURSOR.lastrowid
        type(self).ALL[self.id] = self

    def update(self):
        # Update this character's table row corresponding to the current Character instance
        sql = """
            UPDATE characters
            SET name = ?, character_class = ?, character_description = ?, xp = ?, hp = ?, mp = ?, power = ?, player_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (
                            self.name, self.character_class, self.character_description, self.xp, self.hp, self.mp, 
                            self.power, self.player_id
                            )
                        )
        CONN.commit()

    def delete(self):
        # Delete this character from database
        sql = """
            DELETE FROM characters
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).ALL[self.id]

        # Set id to None
        self.id = None

    @classmethod
    def create(cls, name, character_class, character_description, xp, hp, mp, power, player_id):
        # Create a new character instance and save it to database row
        character = cls(name, character_class, character_description, xp, hp, mp, power, player_id)
        character.save()
        return character

    @classmethod
    def instance_from_db(cls, row):
        print("database row:", row)
        # Return a character object with attributes from correct table row

        # Check the dictionary for an existing instance using the row's primary key
        character = cls.ALL.get(row[0])
        if character:
            # ensure attributes match row values in case local instance was modified
            character.name = row[1]
            character.character_class = row[2]
            character.character_description = row[3]
            character.xp = row[4]
            character.hp = row[5]
            character.mp = row[6]
            character.power = row[7]
            character.player_id = row[8]
        else:
            # not in dictionary, create new instance and add to dictionary
            character = cls(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
            character.id = row[0]
            cls.ALL[character.id] = character
        return character

    @classmethod
    def get_all(cls):
        # Return a list containing all character instances
        sql = """
            SELECT *
            FROM characters
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        # Find a character by their ID
        sql = """
            SELECT *
            FROM characters
            WHERE id = ?
        """
        # Return Character object from the table row with matching primary key
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        # Find a character by their name
        sql = """
            SELECT *
            FROM characters
            WHERE name is ?
        """
        # Return the first table row of a Character object matching a name
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    # @classmethod
    # def is_name_unique(cls, name):
    #     # Search in-memory
    #     is_unique_in_memory = not any(player.name == name for player in cls.ALL.values())

    #     # Search in database
    #     sql = """
    #         SELECT * 
    #         FROM characters
    #         WHERE name is ?
    #     """
    #     row = CURSOR.execute(sql, (name,)).fetchone()
    #     is_unique_in_db = row is None

    #     # if a result, return False; else: return True
    #     return is_unique_in_db and is_unique_in_memory
