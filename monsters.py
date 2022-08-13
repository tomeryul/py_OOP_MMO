from party import *


class Monster:
    def __init__(self, name, exp, max_hp):
        self.name = name
        self.exp = exp
        self.max_hp = max_hp
        self.current_hp = max_hp

    def monster_attacked_solo(self, character):
        time_to_kill = 0
        power = max(character.skills.values()) + character.weapon_power

        while self.current_hp > 0:
            self.current_hp -= power
            time_to_kill += 1

        self.current_hp = self.max_hp
        return time_to_kill

    def monster_attacked_party(self, party):
        time_to_kill = 0
        power = 0
        for member in party.the_party:
            power += max(member.skills.values()) + member.weapon_power

        while self.current_hp > 0:
            self.current_hp -= power
            time_to_kill += 0.5

        self.current_hp = self.max_hp
        return time_to_kill
