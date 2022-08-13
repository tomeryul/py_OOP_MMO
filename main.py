from MMO_world import *
import pickle

file_name = "World.bin"


def save_to_file(file, my_party):
    pickle.dump(my_party, open(file, "wb"))


def load_from_file(file):
    chara = pickle.load(open(file, "rb"))
    return chara


def menu():
    print(f'(1) Create character\n'
          f'(2) Create monster\n'
          f'(3) Create map\n'
          f'(4) Enter to a new party\n'
          f'(5) Create new party\n'
          f'(6) Exit from party\n'
          f'(7) Send single character to train\n'
          f'(8) Send a party to train\n'
          f'(9) Open Chests\n'
          f'(10) Show the wold info\n'
          f'(0) Save and exit')


my_world = None
file_lode_option = input("do you wont to load from last time? (yes/no): ")

if file_lode_option.lower() == "yes":
    my_world = load_from_file(file_name)

else:
    my_world = TheWorld("T_MMO")
    my_world.arr_of_characters.append(Warrior("Omer"))
    my_world.arr_of_characters.append(Thif("Nadav"))
    my_world.arr_of_characters.append(Magician("Omri"))
    my_world.arr_of_parties.append(Party("The Beasts"))
    my_world.arr_of_parties.append(Party("The Jokers"))
    my_world.arr_of_monsters.append(Monster("Slim", 20, 100))
    my_world.arr_of_monsters.append(Monster("Orange Mushroom", 30, 120))
    my_world.arr_of_monsters.append(Monster("Zombie Mushroom", 50, 200))
    my_world.arr_of_monsters.append(Monster("Goloms", 60, 250))
    my_world.arr_of_maps.append(Map("First Map", my_world.arr_of_monsters[0]))
    my_world.arr_of_maps.append(Map("Second Map", my_world.arr_of_monsters[1]))
    my_world.arr_of_maps.append(Map("Third Map", my_world.arr_of_monsters[2]))
    my_world.arr_of_maps.append(Map("Forth Map", my_world.arr_of_monsters[3]))
    my_world.arr_of_parties[1].add_to_party(my_world.arr_of_characters[1])
    my_world.arr_of_parties[1].add_to_party(my_world.arr_of_characters[2])

while True:
    menu()
    option = int(input("enter your option: "))
    if option == 1:
        my_world.create_character()
    elif option == 2:
        my_world.create_monster()
    elif option == 3:
        my_world.create_map()
    elif option == 4:
        my_world.create_party()
    elif option == 5:
        my_world.join_party()
    elif option == 6:
        my_world.exit_party()
    elif option == 7:
        my_world.solo_training()
    elif option == 8:
        my_world.party_training()
    elif option == 9:
        my_world.open_chests()
    elif option == 10:
        my_world.wold_info()

    elif option == 0:
        save_to_file(file_name, my_world)
        print("come back soon!!\n")
        break
    else:
        print(f'Not valid option!\n')
