from job import *


class Party:
    def __init__(self, name):
        self.name = name
        self.the_party = []
        self.max = 5
        self.num_of_members = 0
        self.occupied = None

    def is_occupied(self):
        if self.occupied is None:
            return False

        my_now = datetime.now()
        now_day, now_hour, now_minute = int(my_now.strftime("%d")), int(my_now.strftime("%H")), int(my_now.strftime("%M"))

        occupied_till_day, occupied_till_hour, occupied_till_minute = self.occupied

        if now_day == occupied_till_day:
            if now_hour == occupied_till_hour:
                if now_minute >= occupied_till_minute:
                    self.occupied = None
                    return False

                else:
                    return True

            elif now_hour < occupied_till_hour:
                return True

            else:
                self.occupied = None
                return False

        elif now_day < occupied_till_day:
            return True

        self.occupied = None
        return False

    def set_occupation(self, num_of_hours):
        my_now = datetime.now()
        day, hour, minute = int(my_now.strftime("%d")), int(my_now.strftime("%H")), int(my_now.strftime("%M"))
        new_day, new_hour, new_minute = day, hour + num_of_hours, minute
        if new_hour >= 24:
            new_hour %= 24
            new_day += 1

        self.occupied = new_day, new_hour, new_minute

    def add_to_party(self, character):
        if self.num_of_members < self.max:
            if self.in_party(character.name) is False:
                self.num_of_members += 1
                self.the_party.append(character)
                character.my_party_name = self.name
            else:
                print("cannot enter to the party because the character already in it")
        else:
            print("cannot enter to the party because its full")

    def in_party(self, character_name):
        for character in self.the_party:
            if character.name == character_name:
                return True

        return False

    def remove_from_party(self, character_name):
        for character in self.the_party:
            if character.name == character_name:
                self.the_party.remove(character)
                self.num_of_members -= 1
                break

    def party_info(self):
        if self.num_of_members == 0:
            print(f'the party named "{self.name}" is empty!!\n')
        else:
            print(f'the party named "{self.name}" have {self.num_of_members} members:')
            if self.is_occupied():
                print(f'"{self.name}" went to trine and will come back at: {self.occupied[0]}th '
                      f'at ({self.occupied[1]}:{self.occupied[2]})'
                      f"\nthere for we don't know their stats correctly:")

            for i in self.the_party:
                i.Character_Info()
