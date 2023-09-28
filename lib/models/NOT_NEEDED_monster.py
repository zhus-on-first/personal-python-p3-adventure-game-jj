# Not needed: not persisting monster states between player encounters or game sessions.

from models.__init__ import CURSOR, CONN

class Monster:
    ALL = {}

    def __init__(self, type, hp, power, healing_item, name=None, id=None):
        self.id = id
        self.name = name
        self.type = type
        self.hp = hp
        self.power = power
        self.healing_item = healing_item
        self.healing_item_used = False

    # Getter and Setter for name
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            raise ValueError("Name must be a string.")

    # Getter and Setter for type
    @property
    def type(self):
        return self._type
    
    @type.setter
    def type(self, type):
        if isinstance(type, str):
            self._type = type
        else:
            raise ValueError("Type must be a string.")

    # Getter and Setter for hp
    @property
    def hp(self):
        return self._hp
    
    @hp.setter
    def hp(self, hp):
        if isinstance(hp, int) and hp >= 0:
            self._hp = hp
        else:
            raise ValueError("hp must be a positive integer.")
        
    # Getter and Setter for Power
    @property
    def power(self):
        return self._power
    
    @power.setter
    def hp(self, power):
        if isinstance(power, int) and power >= 0:
            self._power = power
        else:
            raise ValueError("Power must be a positive integer.")

    # Getter and Setter for healing_item
    @property
    def healing_item(self):
        return self._healing_item
    
    @healing_item.setter
    def healing_item(self, item):
        if isinstance(item, str):
            self._healing_item = item
        else:
            raise ValueError("Healing item must be a string.")

    # Getter for healing_item_used (no setter since immutable: used once)
    @property
    def healing_item_used(self):
        return self._healing_item_used

    # Method to use the healing item
    def use_healing_item(self):
        if not self._healing_item_used:
            self._healing_item_used = True
            # logic to use healing
        else:
            print("Healing item already used.")

    # CRUD methods for Monster class below
    @classmethod
    def create_table(cls):
        sql = """ CREATE TABLE IF NOT EXISTS monsters (
                  id INTEGER PRIMARY KEY,
                  name TEXT,
                  type TEXT,
                  hp INTEGER,
                  power INTEGER,
                  healing_item BOOLEAN)
              """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        sql = """DROP TABLE IF EXISTS monsters"""
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """INSERT INTO monsters (name, type, hp, power, healing_item)
                 VALUES (?, ?, ?)"""
        CURSOR.execute(sql, (
                            self.name, self.type, self.hp, self.power, self.healing_item
                            )
                        )
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).ALL[self.id] = self

    def update(self):
        sql = """UPDATE monsters
                 SET name = ?, type = ?, hp = ?, power =?, healing_item = ?
                 WHERE id = ?"""
        CURSOR.execute(sql, (
                            self.name, self.type, self.hp, self.power, 
                            self.healing_item, self.id)
                        )
        CONN.commit()

    def delete(self):
        sql = """DELETE FROM monsters WHERE id = ?"""
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).ALL[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        monster = cls.ALL.get(row[0])
        if monster:
            monster.name = row[1]
            monster.type = row[2]
            monster.hp = row[3]
            monster.power = row[4]
            monster.healing_item = row[5]
        else:
            monster = cls(row[1], row[2], row[3], row[4], row[5])
            monster.id = row[0]
            cls.ALL[monster.id] = monster
        return monster

    @classmethod
    def get_all(cls):
        sql = """SELECT * FROM monsters"""
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = """SELECT * FROM monsters WHERE id = ?"""
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

