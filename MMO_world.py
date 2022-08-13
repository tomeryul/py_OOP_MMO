from MMO_Map import *
import random


def get_name(my_str, arr):
    while True:
        Already_exists = False
        name = str(input(my_str))

        for arr_object in arr:
            if arr_object.name.lower() == name:
                Already_exists = True

        if Already_exists:
            print(f'the name "{name}" already exists choose again.')
        else:
            break
    name = " ".join(list(map(lambda x: "".join([x[letter].upper()
                                                if letter == 0 else x[letter] for letter in range(len(x))]),
                             name.split(" "))))
    return name


def get_number(my_str, arr):
    while True:
        print(my_str)
        for i in range(len(arr)):
            print(f'({i + 1}) for "{arr[i].name}"')
        answer = int(input(""))

        if answer == -1:
            return -1

        if 1 <= answer <= len(arr):
            break

    return answer - 1


def get_map_and_hours(arr_of_maps):
    while True:
        map_number = get_number("enter a number that represent the map you want to train in (-1 to exit):", arr_of_maps)

        if map_number == -1:
            return -1, -1

        answer = input(f'The map you chose have the monster "{arr_of_maps[map_number].monsters.name}" that '
                       f'gives '
                       f'{arr_of_maps[map_number].monsters.exp} EXP, is it ok? (yes, no): ').lower()

        if answer == "yes":
            break

    while True:
        str_answer = input("Enter the time you want to train in hours (only integers from 1 to 9): ")

        if len(str_answer) == 1:
            ord_num = ord(str_answer) - 48  # "0" in ascii table is 48
            if 1 <= ord_num <= 9:
                break

    return map_number, int(str_answer)


class TheWorld:
    def __init__(self, name):
        self.name = name
        self.arr_of_characters = []
        self.arr_of_parties = []
        self.arr_of_monsters = []
        self.arr_of_maps = []

    def wold_info(self):
        print(f'\nThe name of this world is: "{self.name}", and it has {len(self.arr_of_characters)} characters')
        print("--" * 30)
        print('the characters that are not in a party:')

        for character in self.arr_of_characters:
            if character.my_party_name is None:
                character.Character_Info()
        print("--" * 30)

        print(f'in this world thar are {len(self.arr_of_parties)} parties:\n')
        for party in self.arr_of_parties:
            party.party_info()
        print("--" * 30)

    def create_character(self):
        character_name = get_name("enter a name for your character:", self.arr_of_characters)

        new_character = None
        arr_of_jobs = ["Warrior", "Thif", "Magician", "Archer"]
        while True:

            for index in range(len(arr_of_jobs)):
                print(f'({index + 1}) for "{arr_of_jobs[index]}"')

            job_num = int(input("enter the number that represent the job you chose:"))

            if 1 <= job_num <= (len(arr_of_jobs)):
                break

        if job_num == 1:
            new_character = Warrior(character_name)

        elif job_num == 2:
            new_character = Thif(character_name)

        elif job_num == 3:
            new_character = Magician(character_name)

        elif job_num == 4:
            new_character = Archer(character_name)

        new_character.Character_Info()
        self.arr_of_characters.append(new_character)

    def create_party(self):
        party_name = get_name("enter a name for your party:", self.arr_of_parties)
        new_party = Party(party_name)
        self.arr_of_parties.append(new_party)
        print("")

    def create_monster(self):
        monster_name = get_name("enter a name for your monster:", self.arr_of_monsters)
        exp = int(input("enter amount of exp from killing the monster:"))
        hp = int(input("enter amount of hp for the monster:"))

        new_monster = Monster(monster_name, exp, hp)
        self.arr_of_monsters.append(new_monster)
        print("")

    def create_map(self):
        map_name = get_name("enter a name for your map:", self.arr_of_maps)
        number = get_number("enter a number that represent the monster you wont to have in the map (-1 to exit):",
                            self.arr_of_monsters)
        if number == -1:
            return
        new_map = Map(map_name, self.arr_of_monsters[number])
        self.arr_of_maps.append(new_map)

    def join_party(self):
        while True:
            number = get_number("enter a number that represent the character you wont to enter a party (-1 to exit):",
                                self.arr_of_characters)

            if number == -1:
                return

            the_character = self.arr_of_characters[number]

            if the_character.is_occupied():
                print("The character went to train there for cannot enter to a party")

            if not the_character.is_occupied():
                break

        while True:
            number = get_number("enter a number that represent the party you wont to enter to (-1 to exit):",
                                self.arr_of_parties)

            if number == -1:
                return

            the_party = self.arr_of_parties[number]

            if the_party.is_occupied():
                print("The party went to train there for you cannot join to this party")

            if not the_party.is_occupied():
                break

        if the_character.my_party_name is not None and the_character.my_party_name is not the_party.name:
            for party in self.arr_of_parties:
                if party.name == the_character.my_party_name:
                    party.remove_from_party(the_character.name)
                    print(f'{the_character.name} exit his last party to enter: "{the_party.name}"')
                    break

        the_party.add_to_party(the_character)
        the_character.my_party_name = the_party.name
        the_party.party_info()

    def exit_party(self):
        while True:
            index = 0
            for character in self.arr_of_characters:
                if character.my_party_name is not None and not character.is_occupied():
                    index += 1
                    print(
                        f'({index}) for character named : "{character.name}", party name: "{character.my_party_name}"')

            if index == 0:
                print("\nAll the characters that in a party went to train there for cannot exit their party"
                      "\nOr all the parties are empty there for no character can exit\n")
                return

            answer = int(input(""))

            if 1 <= answer <= index:
                break

        the_character = None
        for character in self.arr_of_characters:
            if character.my_party_name is not None and not character.is_occupied():
                answer -= 1
                if answer == 0:
                    the_character = character
                    break

        the_party_name = the_character.my_party_name
        the_character.my_party_name = None

        the_party = None
        for party in self.arr_of_parties:
            if party.name == the_party_name:
                the_party = party
                break

        the_party.remove_from_party(the_character.name)

    def solo_training(self):

        while True:
            character_number = get_number("enter a number that represent the character you want to train (-1 to exit):",
                                          self.arr_of_characters)

            if character_number == -1:
                return

            elif self.arr_of_characters[character_number].is_occupied() is True:
                print("character went to train already!")

            elif self.arr_of_characters[character_number].my_party_name is not None:
                print("character in a party there for, cannot go to train alone!")

            else:
                break

        map_number, hours = get_map_and_hours(self.arr_of_maps)

        if map_number == -1:
            return

        self.arr_of_characters[character_number].num_of_chests_to_open += hours

        self.arr_of_maps[map_number].solo_training(hours, self.arr_of_characters[character_number])

    def party_training(self):
        while True:
            party_number = get_number("enter a number that represent the party you wont to train (-1 to exit):",
                                      self.arr_of_parties)

            if party_number == -1:
                return

            if self.arr_of_parties[party_number].is_occupied() is True:
                print("party went to train already!")

            elif self.arr_of_parties[party_number].num_of_members == 0:
                print("the party you chose is empty!")

            else:
                break

        map_number, hours = get_map_and_hours(self.arr_of_maps)

        for character in self.arr_of_parties[party_number].the_party:
            character.num_of_chests_to_open += hours

        self.arr_of_maps[map_number].party_training(hours, self.arr_of_parties[party_number])

    def open_chests(self):
        while True:
            index = 0
            for character in self.arr_of_characters:
                if character.num_of_chests_to_open > 0 and not character.is_occupied():
                    index += 1
                    print(f'type ({index}) to open {character.num_of_chests_to_open} chests for character named : '
                          f'"{character.name}"')

            if index == 0:
                print("\nit seems like no character can open a chest at the moment\n")
                return

            answer = int(input(""))

            if 1 <= answer <= index:
                break

        the_character = None
        for character in self.arr_of_characters:
            if character.num_of_chests_to_open > 0 and not character.is_occupied():
                answer -= 1
                if answer == 0:
                    the_character = character
                    break

        for i in range(the_character.num_of_chests_to_open):
            new_power = the_character.calc_weapon_power(random.randint(1, 1000))
            print(f'({i + 1}) {the_character.name} got a weapon with power of {new_power}')
            the_character.weapon_power = new_power
        the_character.num_of_chests_to_open = 0
        print()
