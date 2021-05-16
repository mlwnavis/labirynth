import Objects
from graph_wyk import Graph
import Tools
from copy import copy
IO = Tools.IO()

Directions = {"N":"S", "S":"N","E":"W","W":"E", "Up":"Down", "Down":"Up"}


class Actions:

    def __init__(self,labirynt):
        self.player = None
        self.labirynt = labirynt

    def add_player(self, player):
        self.player = player

    def move(self, room, action):
        if len(action) == 1:
            self.labirynt.move(action[0])
            cur_room = self.labirynt.get_cur_room()
            if cur_room == room:
                pass
            else:
                shop = True if type(cur_room) == s else False
                enemy = cur_room.get_enemy()
                IO.examine_room(cur_room, enemy, shop, cur_room.get_staircase(), cur_room.get_gold())
                if enemy is not None:
                    if not enemy.is_aware():
                        enemy.become_aware()
                    else:
                        Walka = Objects.Combat(cur_room, self.player, enemy)
                        while self.player.get_hit_points() > 0 and enemy.get_hit_points() > 0:
                            Walka.turn()
        else:
            IO.wrong_action()

    def fight(self,room, action):
        if len(action) == 1:
            if room.get_enemy() is not None:
                enemy = room.get_enemy()
                IO.player_attacks(self.player, enemy)
                Walka = Objects.Combat(room, self.player, enemy, bonus=5)
                while self.player.get_hit_points() > 0 and enemy.get_hit_points() > 0:
                    Walka.turn()
            else:
                IO.wrong_action()
        else:
            IO.wrong_action()

    def examine(self,room, action):
        if len(action) == 1:
            shop = True if type(room) == Shop else False
            enemy = room.get_enemy()
            IO.examine_room(room, enemy, shop, room.get_staircase(), room.get_gold())
        else:
            IO.wrong_action()

    def pick_up(self, room, action):
        if len(action) == 1:
            IO.not_enough_info(action[0])
        else:
            if type(room) is Shop:
                IO.theft_prevention()
                pass
            ground = room.get_ground()

            thing = action[1].capitalize()
            if thing == "Wszystko":
                for item in ground:
                    room.pick_from_ground(self.player, item)
                    amount = room.get_gold()
                    if amount > 0:
                        room.pick_gold_from_ground(self.player)

            elif thing == "Złoto":
                amount = room.get_gold()
                if amount < 1:
                    IO.no_gold_on_ground()
                else:
                    room.pick_gold_from_ground(self.player)

    def open(self, room, action):

        if room.get_chest() is not None and len(action) == 1:
            chest = room.get_chest()
            if chest.get_opened():
                IO.open_chest(chest, opened=True)
            else:
                if chest.get_lock():
                    unlocked = False
                    for item in self.player.get_equipment():
                        if str(item) == "Klucz":
                            unlocked = True
                            self.player.use_item(item)
                            IO.open_chest(chest, key=True)
                            action = IO.action(chest=True).capitalize()
                            if action == "Tak":
                                chest.take_loot(self.player)
                                IO.loot_chest()
                            elif action == "Nie":
                                IO.leave_chest()
                                chest.dump_on_the_ground(room)
                            else:
                                IO.wrong_action()
                            break
                    if not unlocked:
                        IO.open_chest(chest, locked=True, key=False)

                else:
                    IO.open_chest(chest, locked=False)
                    action = IO.action(chest=True).capitalize()
                    if action == "Tak":
                        chest.take_loot(self.player)
                        IO.loot_chest()
                    elif action == "Nie":
                        IO.leave_chest()
                        chest.dump_on_the_ground(room)
                    else:
                        IO.wrong_action()

        else:
            IO.wrong_action()

    def equip(self, room, action):
        if len(action) == 1:
            IO.not_enough_info(action[0])

        elif len(action) >3:
            IO.wrong_action()

        else:
            thing = " ".join(action[1:]).capitalize()
            got_it = False
            if thing in Objects.Items:
                for item in self.player.get_equipment():
                    if str(item) == thing:
                        print(thing)
                        if str(item) in Objects.Weapons:
                            got_it = True
                            self.player.equip_weapon(item)
                            break
                if not got_it:
                    IO.wrong_item(self.player)
            else:
                IO.wrong_item_name()

    def show(self, room, action):
        if len(action) == 1:
            IO.not_enough_info(action[0])

        elif len(action) >3:
            IO.wrong_action()

        else:
            thing = action[1].capitalize()
            if thing == "Broń":
                IO.show_equipped_weapon(self.player)
            elif thing == "Ekwipunek":
                IO.show_equipment(self.player)

            else:
                IO.wrong_action()

    def help(self, room, action):
        if len(action) == 1:
            chest, ground, enemy = False, False, False
            if room.get_chest() != None: chest = True
            if room.get_ground() != []: ground = True
            if room.get_enemy() != None: enemy = True
            IO.help(chest=chest, ground=ground, enemy=enemy)
        else:
            IO.wrong_action()

    def destroy(self, room, action):
        if len(action) == 1:
            chest = room.get_chest()
            if chest is None:
                IO.wrong_action()
            elif not chest.get_break():
                IO.break_chest(breakable=False)
            elif chest.get_tried_to_break():
                IO.break_chest(tried=True)
            elif chest.get_broken():
                IO.break_chest(broken=True)
            else:
                chest.try_to_break()
                req = 30 if self.player.get_equipped() is None else 20
                if self.player.take_test("K") >= req:
                    chest.break_chest(room)
                    IO.break_chest(success=True, player=self.player)
                else:
                    IO.break_chest(success=False, player=self.player)
        else:
            IO.wrong_action()

    def buy(self, room, action):
        if len(action) == 1:
            IO.not_enough_info(action[0])
        else:
            if type(room) == s:
                thing = " ".join(action[1:]).capitalize()
                if thing in Objects.Items:
                    room.buy(self.player, thing)
                else:
                    IO.wrong_item_name()
            else:
                IO.not_in_shop()

class Room:

    def __init__(self, coordinates, chest = None, enemy = None, ground = []):
        self.chest = chest
        self.enemy = enemy
        self.ground = ground
        self.gold = 0
        self.status = 0
        self.neighbours = {}
        self.staircase = False
        self.coordinates = coordinates


    def add_neighbour(self, room, direction):
        self.neighbours[direction] = room

    def set_staircase(self):
        self.staircase = True

    def remove_enemy(self):
        self.enemy = None

    def discover(self):
        self.status = 1

    def pick_gold_from_ground(self, player):
        player.add_gold(self.gold)
        IO.picked_gold_from_ground(player, self.gold)
        self.gold = 0


    def pick_from_ground(self, player, item):
        player.add_equipment(item)
        self.ground.remove(item)
        IO.picked_from_ground(player, item)

    def drop_gold_to_ground(self, amount):
        self.gold += amount

    def drop_to_ground(self, item):
        self.ground.append(item)

    def get_staircase(self):
        return self.staircase

    def get_status(self):
        return self.status

    def get_neighbours(self):
        return self.neighbours

    def get_enemy(self):
        return self.enemy

    def get_chest(self):
        return self.chest

    def get_ground(self):
        return self.ground

    def get_gold(self):
        return self.gold

    def get_coords(self):
        return self.coordinates

    def __str__(self):
        return(str(self.coordinates))

class Shop(Room):

    def __init__(self,coordinates, stock):
        super().__init__(coordinates, ground = stock)

    def get_stock(self):
        return self.ground

    def buy(self, player, item):
        price = Objects.Items[item]['price']
        got_it = False
        for offert in self.ground:
            if str(offert) == item:
                if price <= player.get_gold():
                    got_it = True
                    player.pay(price)
                    player.add_equipment(offert)
                    self.ground.remove(offert)
                    IO.buy(player, offert)
                else:
                    IO.not_enough_gold()
        if not got_it:
            IO.not_in_stock()

class Labirynth:

    def __init__(self):
        self.rooms = Graph()
        self.start_room = None
        self.cur_room = None

    def add_room(self,room, neighbours):
        if self.start_room is None:
            self.start_room = room
            self.cur_room = room
        for neighbour in neighbours:
            self.rooms.add_edge(room, neighbour[0])
            self.rooms.add_edge(neighbour[0], room)
            room.add_neighbour(neighbour[0],neighbour[1])
            neighbour[0].add_neighbour(room, Directions[neighbour[1]])

    def show_rooms(self):
        for v in self.rooms:
            print(v)

    def get_rooms(self):
        return self.rooms

    def move(self, direction):
        if direction in self.cur_room.get_neighbours():
            self.cur_room = self.cur_room.get_neighbours()[direction]
        else:
            IO.wrong_action()

    def get_cur_room(self):
        return self.cur_room

    def start(self, act):

        IO.start()
        actions = act
        Actions_dict = {"N": actions.move, "S": actions.move, "W": actions.move, "E": actions.move,
                        "Down": actions.move, "Up": actions.move,
                        "Walcz": actions.fight, "Kup": actions.buy, "Rozejrzyj": actions.examine,
                        "Podnieś": actions.pick_up, "Otwórz": actions.open, "Ekwipuj": actions.equip,
                        "Pomoc": actions.help, "Pokaż": actions.show}
        player = Objects.Player("Garil")
        actions.add_player(player)

        while True:
            IO.show_neighbours(self.cur_room)
            action = IO.action().capitalize().split()
            while len(action) < 1:
                action = IO.action().capitalize().split()
            activity = action[0]
            if activity in Actions_dict:
                Actions_dict[activity](self.cur_room, action)
            else:
                IO.wrong_action()
if __name__ == "__main__":
    Pokoj1 = Room(coordinates=(0,0))
    Goblin = Objects.Monster("Goblin", weapon=Objects.Weapon("Sztylet"), gold=5)
    Pokoj2 = Room(coordinates=(1,0),chest=Objects.Chest(loot=[Objects.Klucz]))
    Pokoj3 = Room(coordinates=(1,1),enemy=Goblin)
    Pokoj4 = Room(coordinates=(0,1),chest=Objects.Chest(loot=[Objects.Weapon("Sztylet")], locked=True, breakable=False))
    Sklep = Shop(coordinates=(1,2),stock=[Objects.Klucz, Objects.Weapon("Miecz jednoręczny")])
    Labirynt = Labirynth()
    Labirynt.add_room(Pokoj1, [[Pokoj2, "E"], [Pokoj4, "N"]])
    Labirynt.add_room(Pokoj2, [[Pokoj3, "N"]])
    Labirynt.add_room(Pokoj3, [[Pokoj4, "W"]])
    Labirynt.add_room(Sklep, [[Pokoj3, "S"]])
    generate = Objects.Generator()
    lab = generate.generate_floor()
    shop = generate.generate_shop((0,1))
    s = type(shop)

    actions = Actions(lab)


    lab.start(actions)
    #Labirynt.start()
