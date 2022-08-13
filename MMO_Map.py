from monsters import *
from party import *


class Map:
    def __init__(self, name, monsters):
        self.name = name
        self.monsters = monsters

    def solo_training(self, time_to_train, character):

        character.set_occupation(time_to_train)
        time_to_train *= 3600  # converting from hours to sec

        while time_to_train > 0:
            time_to_train -= self.monsters.monster_attacked_solo(character)
            character.got_exp(self.monsters.exp)

    def party_training(self, time_to_train, party):

        party.set_occupation(time_to_train)
        for character in party.the_party:
            character.set_occupation(time_to_train)

        time_to_train *= 3600  # converting from hours to sec

        while time_to_train > 0:
            time_to_train -= self.monsters.monster_attacked_party(party)
            for member in party.the_party:
                member.got_exp(self.monsters.exp * 1 / party.num_of_members)










