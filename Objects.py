
from time import sleep
from Tools import IO
import random
import Labirynth
import bfs as bfe

Creatures = {"Garil":{"stats":{"WW":39, "US":31, "K":40,"ODP":43,"ZR":16,"CHA":26,
                       "A":2,"S":4,"HP":14,"WT":4},'type': 'hero', "gold":5,"eq":["Miecz oburęczny"]},
             "Goblin":{"stats":{"WW":25, "US":30, "K":30,"ODP":30,"ZR":25,"SW":20,
                        "A":1,"S":3,"HP":8,"WT":3},'type': 'humanoid', "diff": 1, "desc":"Opis"},
             "Zombi":{"stats":{"WW":25, "US":0, "K":35,"ODP":35,"ZR":10,"SW":0,
                        "A":1,"S":3,"HP":12,"WT":3},'type': 'undead', "diff": 1, "desc":"Opis"},
             "Szkielet":{"stats":{"WW":25, "US":20, "K":30,"ODP":30,"ZR":25,"SW":0,
                        "A":1,"S":3,"HP":10,"WT":3},'type': 'undead', "diff": 1, "desc":"Opis"},
             "Olbrzymi szczur":{"stats":{"WW":25, "US":0, "K":31,"ODP":30,"ZR":42,"SW":18,
                        "A":1,"S":3,"HP":7,"WT":3},'type': 'beast', "diff": 1, "desc":"Opis"},
             "Ork":{"stats":{"WW":35, "US":35, "K":35,"ODP":45,"ZR":25,"SW":30,
                        "A":1,"S":3,"HP":12,"WT":4},'type': 'humanoid', "diff": 2, "desc":"Opis"},
             "Ghul":{"stats":{"WW":32, "US":0, "K":37,"ODP":45,"ZR":34,"SW":31,
                        "A":2,"S":3,"HP":11,"WT":4},'type': 'humanoid', "diff": 2, "desc":"Opis"},
             "Upiorny wilk":{"stats":{"WW":35, "US":0, "K":41,"ODP":35,"ZR":18,"SW":0,
                        "A":1,"S":4,"HP":10,"WT":3},'type': 'beast', "diff": 2, "desc":"Opis"},
             "Minotaur":{"stats":{"WW":42, "US":25, "K":48,"ODP":46,"ZR":38,"SW":24,
                        "A":2,"S":4,"HP":26,"WT":4},'type': 'humanoid', "diff": 3, "desc":"Opis"},
             "Zębacz":{"stats":{"WW":42, "US":0, "K":53,"ODP":35,"ZR":56,"SW":22,
                        "A":2,"S":5,"HP":10,"WT":4},'type': 'beast', "diff": 3, "desc":"Opis"},
             "Szczurogr": {"stats": {"WW": 36, "US": 0, "K": 52, "ODP": 47, "ZR": 25, "SW": 17,
                        "A": 3, "S": 5, "HP": 28, "WT": 4}, 'type': 'beast', "diff": 4, "desc": "Opis"}}

Monsters = {"Goblin":{"stats":{"WW":25, "US":30, "K":30,"ODP":30,"ZR":25,"SW":20,
                        "A":1,"S":3,"HP":8,"WT":3},'type': 'humanoid', "diff": 1, "desc":"Opis"},
             "Zombi":{"stats":{"WW":25, "US":0, "K":35,"ODP":35,"ZR":10,"SW":0,
                        "A":1,"S":3,"HP":12,"WT":3},'type': 'undead', "diff": 1, "desc":"Opis"},
             "Szkielet":{"stats":{"WW":25, "US":20, "K":30,"ODP":30,"ZR":25,"SW":0,
                        "A":1,"S":3,"HP":10,"WT":3},'type': 'undead', "diff": 1, "desc":"Opis"},
             "Olbrzymi szczur":{"stats":{"WW":25, "US":0, "K":31,"ODP":30,"ZR":42,"SW":18,
                        "A":1,"S":3,"HP":7,"WT":3},'type': 'beast', "diff": 1, "desc":"Opis"},
             "Ork":{"stats":{"WW":35, "US":35, "K":35,"ODP":45,"ZR":25,"SW":30,
                        "A":1,"S":3,"HP":12,"WT":4},'type': 'humanoid', "diff": 2, "desc":"Opis"},
             "Ghul":{"stats":{"WW":32, "US":0, "K":37,"ODP":45,"ZR":34,"SW":31,
                        "A":2,"S":3,"HP":11,"WT":4},'type': 'humanoid', "diff": 2, "desc":"Opis"},
             "Upiorny wilk":{"stats":{"WW":35, "US":0, "K":41,"ODP":35,"ZR":18,"SW":0,
                        "A":1,"S":4,"HP":10,"WT":3},'type': 'beast', "diff": 2, "desc":"Opis"},
             "Minotaur":{"stats":{"WW":42, "US":25, "K":48,"ODP":46,"ZR":38,"SW":24,
                        "A":2,"S":4,"HP":26,"WT":4},'type': 'humanoid', "diff": 3, "desc":"Opis"},
             "Zębacz":{"stats":{"WW":42, "US":0, "K":53,"ODP":35,"ZR":56,"SW":22,
                        "A":2,"S":5,"HP":10,"WT":4},'type': 'beast', "diff": 3, "desc":"Opis"},
             "Szczurogr": {"stats": {"WW": 36, "US": 0, "K": 52, "ODP": 47, "ZR": 25, "SW": 17,
                        "A": 3, "S": 5, "HP": 28, "WT": 4}, 'type': 'beast', "diff": 4, "desc": "Opis"}
            }

Items = {"Klucz": {"type": 'usable', 'price': 5},
         "Sztylet":{'type':'weapon',"price": 7, 'dmg':-2},
         "Miecz jednoręczny":{'type': "weapon",'price':10, 'dmg':0},
         "Miecz oburęczny":{'type': "weapon",'price':20, 'dmg':2},
         "Kij":{'type': "weapon",'price':5, 'dmg':-3},
         "Korbacz":{'type': "weapon",'price':15, 'dmg':1}}

Weapons = {"Sztylet":{'type':'weapon',"price": 7, 'dmg':-2},
         "Miecz jednoręczny":{'type': "weapon",'price':10, 'dmg':0},
         "Miecz oburęczny":{'type': "weapon",'price':20, 'dmg':2},
         "Kij":{'type': "weapon",'price':5, 'dmg':-3},
         "Korbacz":{'type': "weapon",'price':15, 'dmg':1}}

IO = IO()

def dice(d):
    return random.randint(1,d+1)

class Generator:

    def __init__(self, p_chest = 0.2, p_enemy = 0.35, floors = 3):
        self.p_chest = p_chest
        self.p_enemy = p_enemy
        self.floors = floors

    def generate_chest(self):
        if random.uniform(0,1) <= self.p_chest:
            tmp = [2, 3, 4]
            n_items = random.choices(tmp, weights=[5, 3, 1], k=1)[0]
            p_closed = 0.25 * n_items
            p_breakable = 1 / 3 * (n_items - 1)
            closed = True if random.uniform(0, 1) <= p_closed else False
            breakable = True if random.uniform(0, 1) <= p_breakable else False
            items = random.sample(list(Items), k=n_items)
            list_of_items = []
            for item in items:
                if Items[item]['type'] == 'weapon':
                    list_of_items.append(Weapon(item))
                else:
                    list_of_items.append(Item(item))

            return Chest(breakable=breakable, locked=closed, loot=list_of_items)
        return None

    def generate_monster(self):
        if random.uniform(0,1) <= self.p_enemy:
            monster = random.sample(list(Monsters), k=1)[0]
            while Creatures[monster]['diff'] >= 3:
                monster = random.sample(list(Monsters), k=1)[0]

            weapon = None
            gold = None

            if Creatures[monster]['type'] == 'humanoid':
                if random.uniform(0, 1) <= 0.3:
                    item = random.sample(list(Weapons), k=1)[0]
                    weapon = Weapon(item)

            if Creatures[monster]['type'] != 'beast':
                gold = random.randint(1, 3) * Creatures[monster]['diff']

            return Monster(monster, gold, weapon)
        return None

    def generate_shop(self, coordinates):
        tmp = random.sample(list(Items), k=random.randint(2,4))
        items = [Item(x) for x in tmp]
        return Labirynth.Shop(coordinates=coordinates, stock=items)



    def generate_room(self, coordinates):
        return Labirynth.Room(coordinates, chest=self.generate_chest(), enemy=self.generate_monster())

    def generate_floor(self):
        changes = {"N":(0,1), "S":(0,-1), "W":(-1,0), "E":(1,0)}

        def generate_corridor(room, len, p_shop):
            if len != 0:
                neighbours = room.get_neighbours()
                directions = [direction for direction in Labirynth.Directions if direction not in neighbours and
                          direction not in ["Up", "Down"]]
                if directions != []:

                    cur_cords = room.get_coords()
                    direction = random.sample(directions, k=1)[0]
                    change = changes[direction]
                    new_cords = (cur_cords[0] + change[0], cur_cords[1] + change[1])
                    if len == 2 and shop == False and p_shop == 1:

                        new_room = self.generate_shop(coordinates=new_cords)
                    else:
                        new_room = self.generate_room(coordinates=new_cords)
                    rooms[new_cords] = new_room
                    list_of_neighbours = []

                    for dir in changes:
                        change2 = changes[dir]
                        if (new_cords[0] + change2[0], new_cords[1] + change2[1]) in rooms:
                            tmp = (new_cords[0] + change2[0], new_cords[1] + change2[1])
                            list_of_neighbours.append([rooms[tmp], dir])

                    rooms[new_cords] = new_room
                    floor.add_room(new_room, list_of_neighbours)
                    generate_corridor(new_room, len - 1, p_shop)

                else:
                    generate_corridor(random.sample(list(neighbours.values()), k=1)[0], len, p_shop)

        def longest_path():
            bfs = bfe.BFS(floor.get_rooms())
            bfs.bfs(starting_room)
            distances = {len(bfs.traverse(room)):room for room in list(rooms.values())}
            while type(distances[max(distances)]) == Labirynth.Shop:
                del distances[max(distances)]
            return distances[max(distances)]


        floor = Labirynth.Labirynth()
        starting_room = Labirynth.Room((0,0))
        floor.add_room(starting_room, [])
        for fl in range(self.floors):
            rooms = {}
            shop = False
            n_of_directions = random.randint(2, 4)
            rooms[(0, 0)] = starting_room
            for n in range(n_of_directions):
                generate_corridor(starting_room, fl + 4, (n + 1) / n_of_directions)
            last_room = longest_path()
            last_room.set_staircase()
            print(last_room)
            new_start = Labirynth.Room((0,0))
            new_start.set_staircase()

            floor.add_room(new_start, [[last_room,"Up"]])
            print(new_start.get_neighbours())
            starting_room = new_start



        return floor



class Item:

    def __init__(self, name):
        self.name = name
        self.type = Items[name]["type"]
        self.price = Items[name]["price"]

    def get_name(self):
        return self.name

    def get_type(self):
        return self.type

    def get_price(self):
        return self.price

    def __str__(self):
        return self.name


class Weapon(Item):

    def __init__(self, name):
        super().__init__(name)
        self.dmg = Items[name]['dmg']

    def get_dmg(self):
        return self.dmg


class Combat:

    def __init__(self, room, player, enemy, bonus = 0):
        self.player_hp = player.get_hit_points()
        self.monster_hp = enemy.get_hit_points()
        self.room = room
        if dice(10) + player.get_stats()["ZR"] + bonus >= dice(10) + enemy.get_stats()["ZR"]:
            self.cur_turn = player
            self.next_turn = enemy
        else:
            self.cur_turn = enemy
            self.next_turn = player

    def turn(self):
        def players_turn():
            activity = IO.action(combat=True)

            if activity == "Atakuj":
                for i in range(self.cur_turn.get_stats()["A"]):
                    if self.cur_turn.take_test() >= 0:
                        damage = self.cur_turn.get_damage()
                        effective_damage = damage - self.next_turn.get_stats()["WT"]
                        if effective_damage < 0:
                            effective_damage = 0
                        weapon = self.cur_turn.get_equipped()
                        if weapon == None:
                            weapon = "Pięści"
                        IO.show_hit(self.cur_turn, weapon, damage, effective_damage)

                        self.next_turn.lose_hit_points(effective_damage)
                        if self.next_turn.get_hit_points() <= 0:
                            IO.show_winner(self.cur_turn)
                            self.room.drop_gold_to_ground(self.next_turn.get_gold())
                            self.room.drop_to_ground(self.next_turn.get_equipped())
                            self.room.remove_enemy()
                            break
                    else:
                        IO.show_no_hit(self.cur_turn)

            elif activity == "Rozbrój":
                if self.next_turn.get_equipped() == None:
                    IO.wrong_action()
                    players_turn()
                else:
                    if self.cur_turn.take_opposite_test(my_stat=self.cur_turn.get_stats()["ZR"],
                                                        enemy_stat=self.next_turn.get_stats()["K"]):
                        self.room.drop_to_ground(self.next_turn.get_equipped())
                        IO.show_dropping(self.next_turn, self.next_turn.get_equipped())
                        self.next_turn.lose_weapon()
                    else:
                        IO.show_failure()

            elif activity == "Pomoc":
                IO.help(combat=True)
                players_turn()

        if type(self.cur_turn) is Player:
            players_turn()

        else:
            for i in range(self.cur_turn.get_stats()["A"]):
                if self.cur_turn.take_test() >= 0:
                    damage = self.cur_turn.get_damage()
                    effective_damage = damage - self.next_turn.get_stats()["WT"]
                    if effective_damage < 0:
                        effective_damage = 0
                    weapon = self.cur_turn.get_equipped()
                    if weapon == None:
                        weapon = "Pięści"
                    IO.show_hit(self.cur_turn, weapon, damage, effective_damage)

                    self.next_turn.lose_hit_points(effective_damage)
                    if self.next_turn.get_hit_points() <= 0:
                        IO.show_winner(self.cur_turn)
                        break
                else:
                    IO.show_no_hit(self.cur_turn)
        self.cur_turn, self.next_turn = self.next_turn, self.cur_turn
        sleep(3)

class Chest:

    def __init__(self, breakable = True, trapped = False, locked = False, loot = []):
        self.breakable = breakable
        self.trapped = trapped
        self.locked = locked
        self.loot = loot
        self.opened = False
        self.tried_to_break = False
        self.broken = False

    def get_trapped(self):
        return self.trapped

    def get_break(self):
        return self.breakable

    def try_to_break(self):
        self.tried_to_break = True

    def get_tried_to_break(self):
        return self.tried_to_break

    def get_loot(self):
        self.opened = True
        return self.loot

    def break_chest(self, room):
        self.broken = True
        for item in self.loot:
            room.drop_to_ground(item)

    def get_broken(self):
        return self.broken

    def get_lock(self):
        return self.locked

    def get_opened(self):
        return self.opened

    def take_loot(self, player):
        result, self.loot = self.loot, []
        for item in result:
            player.add_equipment(item)

    def dump_on_the_ground(self, room):
        result, self.loot = self.loot, []
        for item in result:
            room.drop_to_ground(item)


class Creature:

    def __init__(self, name, weapon = None):
        self.name = name
        self.stats = Creatures[name]["stats"]
        self.max_hit_points = Creatures[name]["stats"]["HP"]
        self.curr_hit_points = Creatures[name]["stats"]["HP"]
        self.equipped = weapon

    def lose_hit_points(self, amount):
        self.curr_hit_points -= amount

    def get_damage(self):
        if self.equipped == None:
            mod = -4
        else:
            mod = self.equipped.get_dmg()
        roll = dice(10)
        while roll % 10 == 0:
            roll += dice(10)
        return roll + self.stats["S"] + mod

    def get_name(self):
        return self.name

    def get_hit_points(self):
        return self.curr_hit_points

    def get_stats(self):
        return self.stats

    def __str__(self):
        return self.name

    def take_test(self, stat="WW"):
        return self.stats[stat] - dice(100)

    def take_opposite_test(self, my_stat, enemy_stat):
        if my_stat - dice(100) >= enemy_stat - dice(100):
            return True
        return False

    def get_equipped(self):
        return self.equipped

class Monster(Creature):
    def __init__(self, name,gold, weapon = None):
        super().__init__(name, weapon)
        self.aware = False
        self.gold = gold

    def examine(self):
        return Creatures[self.name]["desc"]

    def get_gold(self):
        return self.gold

    def lose_weapon(self):
        self.equipped = None

    def is_aware(self):
        return self.aware

    def become_aware(self):
        self.aware = True

class Player(Creature):

    def __init__(self, name):
        super().__init__(name)
        self.gold = Creatures[name]["gold"]
        self.equipment = Creatures[name]["eq"]

    def gain_hit_points(self, amount):
        self.curr_hit_points += amount

        if self.max_hit_points < self.curr_hit_points:
            self.curr_hit_points = self.max_hit_points

    def get_gold(self):
        return self.gold

    def add_gold(self, amount):
        self.gold += amount

    def pay(self, amount):
        self.gold -= amount

    def get_equipment(self):
        return self.equipment

    def add_equipment(self, item):
        self.equipment.append(item)

    def equip_weapon(self, weapon):
        if weapon in self.equipment and type(weapon) is Weapon:
            if self.equipped is not None:
                self.equipment.append(self.equipped)
            self.equipment.remove(weapon)
            self.equipped = weapon
            IO.show_equipping(self.name, weapon)
        elif weapon not in self.equipment:
            IO.wrong_item(self.name)
        else:
            IO.wrong_action()

    def drop_item(self, item):
        if item in self.equipment:
            self.equipment.remove(item)
            IO.show_dropping(self.name, item)
        elif item == self.equipped:
            self.equipped = None
            IO.show_dropping(self.name, item)
        else:
            IO.wrong_item(self.name)

    def use_item(self, item):
        self.equipment.remove(item)



Klucz = Item("Klucz")
Sztylet = Weapon("Sztylet")

if __name__ == "__main__":

    Sztylet = Item("Sztylet")
    Sztylet2 = Weapon("Sztylet")
    Garil = Player("Garil")
    Garil.add_equipment(Klucz)
    Garil.add_equipment(Sztylet)
    Garil.add_equipment(Sztylet2)
    Garil.equip_weapon(Sztylet)


    Skrzynia = Chest(loot=[Klucz])


    generate = Generator()
    test = generate.generate_floor()
    for room in test.get_rooms():
        print(room)
    shop = generate.generate_shop((0, 1))
    print(type(shop) is Labirynth.Shop)

