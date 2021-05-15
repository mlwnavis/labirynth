from time import sleep

#class Generator:




class IO:

    #metody dla labiryntu
    def show_neighbours(self, room):
        print("-----")
        print("Dostępne kierunki:")
        for neighbour in room.get_neighbours():
            print("-{}".format(neighbour))

    def examine_room(self, room, enemy, shop, staircase, gold):
        print("-----")
        ground, chest = room.get_ground(), room.get_chest()

        if shop is True:
            print("Wchodzisz do sklepu. Na półkach widzisz:")
            for item in ground:
                print("-{} Cena: {}".format(item, item.get_price()))

        elif gold > 0:
            print("Na ziemi leży {} złota.".format(gold))

        elif staircase is True:
            direction = "w górę" if "Up" in room.get_neighbours() else "w dół"
            print("W pomieszczeniu widzisz schody prowadzące {}".format(direction))

        elif enemy is not None:
            if enemy.get_equipped() is None:
                print("Po pokoju przechadza się {} bez żadnej broni.".format(enemy).capitalize())
            else:
                print("Po pokoju przechadza się {}, dzierży {}.".format(enemy, enemy.get_equipped()).capitalize())
            if not enemy.is_aware():
                print(
                    "{} zdał sobie sprawę z twojej obecności, masz szansę uciec, lub zaatakować go korzystając z zaskoczenia.".format(
                        enemy))
            else:
                print("{} atakuje Cię!".format(enemy))
        elif ground and not shop:
            print("Na ziemii leżą: ")
            for item in ground:
                print("-{} ".format(item))
        elif chest is not None:
            if chest.get_opened():
                print("W pokoju dostrzegasz otwartą wcześniej skrzynię.")
            else:
                print("W pokoju dostrzegasz skrzynię.")
        else:
            print("W pokoju nie ma nic ciekawego.")



    def break_chest(self, breakable = True, tried = False, broken = False, success = False, player = None):
        print("-----")
        if breakable == False:
            print("Nie możesz zniszczyć tej skrzyni.")
        elif tried == True:
            print("Postać próbowała już zniszczyc tę skrzynię.")
        elif broken == True:
            print("Ta skrzynia jest już zniszczona")
        else:
            print("{} próbuje zniszczyć skrzynię...".format(player))
            sleep(2)
            if success == False:
                print("Lecz jedynie wgniata ją lekko.")
            else:
                print("Po kilku uderzeniach ze skrzyni zostają drzazgi, a zawartość ląduje pod nogami bohatera.")


    def open_chest(self, chest, locked = False, key = False, opened = False):
        print("-----")
        if locked is False or key is True:
            if key is True:
                print("Używasz klucza do otwarcia skrzyni...")
            else:
                print("Udaje Ci się otworzyć skrzynię...")
            sleep(2)
            if chest.get_trapped():
                print("Pułapka")
            else:
                if chest.get_loot():
                    print("Wewnątrz znajdują się: ")
                    for item in chest.get_loot():
                        print("-{}".format(item))
                else:
                    print("Skrzynia jest pusta.")

        elif locked is True:
            print("Próbujesz otworzyć skrzynię lecz jest zamknięta. Potrzebujesz klucza.")
            if chest.get_break():
                print("Możesz też spróbować otworzyć ją siłą...")

        elif opened is True:
            print("Skrzynia jest już otwarta.")


    def loot_chest(self):
        print("-----")
        print("Zabierasz wszystkie przedmioty ze skrzyni.")

    def leave_chest(self):
        print("-----")
        print("Zostawiasz skrzynię w spokoju (zawartość będzie traktowana jako leżąca na ziemii).")

    def no_gold_on_ground(self):
        print("-----")
        print("Na ziemi nie ma złota.")

    def picked_gold_from_ground(self, player, amount):
        print("-----")
        print("{} podniósł z ziemi {} złota.".format(player, amount))

    def picked_from_ground(self, player, item):
        print("-----")
        print("{} podniósł {} z ziemi.".format(player, item).capitalize())

    def buy(self, player, item):
        print("-----")
        print("{} zakupił {}.".format(player, item))

    def theft_prevention(self):
        print("-----")
        print("Nie kradnij.")

    def not_enough_gold(self):
        print("-----")
        print("Nie masz wystarczająco dużo złota.")

    def not_in_stock(self):
        print("-----")
        print("Tego przedmiotu nie ma w sklepie.")

    #metody dla gracza
    def show_equipment(self, player):
        print("-----")
        if player.get_gold() == 0:
            print("{} nie ma w sakiewce ani jednej monety.\n".format(player))
        else:
            print("{} ma w sakiewce {} złota.\n".format(player, player.get_gold()))
        if player.get_equipment():
            print("Ekwipunek {}:".format(player))
            for item in player.get_equipment():
                print("-{}".format(item))
        else:
            print("Garil nie ma przy sobie niczego.\n")

    def show_equipped_weapon(self, player):
        print("-----")
        print("{} dzierży {}".format(player, player.get_equipped()).capitalize())

    def show_equipping(self, player, item):
        print("-----")
        print("{} ekwipuje {}.".format(player, item).capitalize())

    def show_dropping(self, player, item):
        print("-----")
        print("{} upuszcza {}.".format(player, item).capitalize())

    def wrong_item(self, player):
        print("-----")
        print("{} nie ma tego przedmiotu w ekwipunku.".format(player))

    #metody dla combatu
    def show_hit(self, attacker, weapon, damage, effective_damage):
        print("-----")
        print("{} trafia {}! Zadaje {} obrażeń (zredukowane do {})."
              .format(attacker, weapon, damage, effective_damage).capitalize())

    def show_no_hit(self, attacker):
        print("-----")
        print("{} nie trafia.".format(attacker))

    def show_winner(self, winner):
        print("-----")
        print("{} wygrał!".format(winner))

    def player_attacks(self,player, enemy):
        print("-----")
        print("{} rzuca się na {}".format(player, enemy).capitalize())

    #metody inne jakies dla giery

    def start(self):
        print("Tutaj będzie fajny narracyjny opis i wgl ale nie ma teraz B)\n Komenda 'Pomoc' istnieje jak cos.")

    def win(self):
        print("Wygrałeś i co dumny jesteś?")

    def lose(self):
        print("f")

    def action(self, chest = False, combat = False):

        if chest == True:
            answer = input("\nChcesz opróżnić skrzynię? Tak/Nie ").capitalize()
            while answer not in ["Tak", "Nie"]:
                answer = input("\nChcesz opróżnić skrzynię? Tak/Nie ").capitalize()
            return answer
        if combat == True:
            answer = input("\nCo chcesz zrobić? ").capitalize()
            while answer not in ["Atakuj", "Rozbrój", "Pomoc"]:
                answer = input("\nCo chcesz zrobić? ").capitalize()
            return answer
        else:
            return input("\nCo chcesz zrobić? ")

    def show_failure(self):
        print("-----")
        print("Akcja kończy się niepowodzeniem.")

    #błędy

    def wrong_item_name(self):
        print("-----")
        print("Taki przedmiot nie istnieje (upewnij się, że poprawnie wpisujesz nazwę).")

    def wrong_action(self):
        print("-----")
        print("Nie możesz tego zrobić!")

    def not_in_shop(self):
        print("-----")
        print("Nie jesteś w sklepie.")

    def not_enough_info(self, activity):
        print("-----")
        if activity == "Podnieś":
            print("Co chcesz podnieść?")
        elif activity == "Pokaż":
            print("Co chcesz zobaczyć?")
        elif activity == "Ekwipuj":
            print("Co chcesz zaekwipować?")
        elif activity == "Kup":
            print("Co chcesz kupić?")

    #pozostałe

    def help(self, combat = False, chest = False, ground = False, enemy = False):
        print("-----")
        print("Możesz wykonać akcje: \n")
        if combat == True:
            print("Atakuj - Postać zaatakuje przeciwnika\n Rozbrój - Postać spróbuje rozbroić przeciwnika")

        else:
            print("N lub S lub W lub E - Postać przejdzie do pokoju znajdującego się w danym kierunku.\n"
                  "Pokaż X - \n   Broń - Pokaże obecnie zaekwipowaną broń\n   Ekwipunek - Pokaże zawartość ekwipunku\n"
                  "Ekwipuj X - Postać ekwipuje X, gdzie X musi być bronią znajdującą się w ekwipunku\n"
                  "Rozejrzyj - Pokaże opis pokoju")


        if chest == True:
            print("Otwórz - Postać spróbuje otworzyć skrzynię znajdującą się w pokoju\n"
                  "Zniszcz - Postać spróbuje otworzyć skrzynię siłą.")

        if ground == True:
            print("Podnieś X - Jeśli chcesz podnieść z ziemi konkretną rzecz, np. Sztylet, Złoto wpisz 'Podnieś Złoto'\n"
                  "Jeśli chcesz podnieść z ziemi wszstko wpisz 'Podnieś Wszystko'")

        if enemy == True:
            print("Walcz - Zaatakujesz przeciwnika (jeśli wyjdziesz z pokoju nie walcząc z przeciwnikiem \n"
                  "następnym razem gdy do niego wejdziesz przeciwnik będzie Cię pamiętał i zaatakuje).")




