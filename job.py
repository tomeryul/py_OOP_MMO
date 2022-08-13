from datetime import datetime


class JobLess:
    def __init__(self, name):
        self.name = name
        self.lvl = 1
        self.amount_fo_exp_to_lvl_up = 100
        self.current_exp = 0
        self.my_party_name = None
        self.occupied = None
        self.weapon_power = self.calc_weapon_power()
        self.num_of_chests_to_open = 0

    def calc_weapon_power(self, number=0):
        if number == 0:
            return 0

        new_weapon_power = -1

        if number == 1:
            new_weapon_power = 100
        if 2 <= number <= 9:
            new_weapon_power = 50
        if 10 <= number <= 49:
            new_weapon_power = 20
        if 50 <= number <= 149:
            new_weapon_power = 10
        if 150 <= number <= 499:
            new_weapon_power = 5
        if 500 <= number <= 1000:
            new_weapon_power = 1

        if new_weapon_power > self.weapon_power:
            return new_weapon_power
        else:
            return self.weapon_power

    def Character_Info(self):
        if self.is_occupied():
            if self.my_party_name is None:
                print(f'"{self.name}" went to trine and will come back at: {self.occupied[0]}th '
                      f'at ({self.occupied[1]}:{self.occupied[2]})'
                      f"\nthere for we don't know his stats correctly:")
            self.Character_Occupied_Info()
        else:
            print(f"\njob: {self.__class__.__name__}\n"
                  f"character name: {self.name}\n"
                  f"lvl: {self.lvl}\n"
                  f"weapon power: {self.weapon_power}")

    def Character_Occupied_Info(self):
        print(f"\njob: {self.__class__.__name__}\n"
              f"character name: {self.name}\n")

    def got_exp(self, exp_got):
        while exp_got >= self.amount_fo_exp_to_lvl_up - self.current_exp:
            exp_got -= self.amount_fo_exp_to_lvl_up - self.current_exp
            self.lvl += 1
            self.amount_fo_exp_to_lvl_up *= 1.2
            self.current_exp = 0

        self.current_exp += exp_got

    def is_occupied(self):
        if self.occupied is None:
            return False

        my_now = datetime.now()
        now_day, now_hour, now_minute = int(my_now.strftime("%d")), int(my_now.strftime("%H")), int(
            my_now.strftime("%M"))

        occupied_till_day, occupied_till_hour, occupied_till_minute = self.occupied

        if now_day == occupied_till_day:
            if now_hour == occupied_till_hour:
                if now_minute >= occupied_till_minute:
                    return False

                else:
                    return True

            elif now_hour < occupied_till_hour:
                return True

            else:
                return False

        elif now_day < occupied_till_day:
            return True

        return False

    def set_occupation(self, num_of_hours):
        my_now = datetime.now()
        day, hour, minute = int(my_now.strftime("%d")), int(my_now.strftime("%H")), int(my_now.strftime("%M"))
        new_day, new_hour, new_minute = day, hour + num_of_hours, minute
        if new_hour >= 24:
            new_hour %= 24
            new_day += 1

        self.occupied = new_day, new_hour, new_minute


class Warrior(JobLess):
    def __init__(self, name):
        super().__init__(name)
        self.skills = self.add_skill()

    def add_skill(self):
        arr_of_skills = {}
        if self.lvl >= 1:
            arr_of_skills["Slash"] = 10
        if self.lvl >= 10:
            arr_of_skills["Jump Attack"] = 50
        if self.lvl >= 50:
            arr_of_skills["Raging Blow"] = 100
        if self.lvl >= 100:
            arr_of_skills["Rage Uprising"] = 150
        return arr_of_skills

    def Character_Info(self):
        super().Character_Info()
        if not self.is_occupied():
            print(f"character skills: {list(self.skills)}\n")

    def got_exp(self, exp_got):
        super().got_exp(exp_got)
        self.skills = self.add_skill()


class Thif(JobLess):
    def __init__(self, name):
        super().__init__(name)
        self.skills = self.add_skill()

    def add_skill(self):
        arr_of_skills = {}
        if self.lvl >= 1:
            arr_of_skills["Shuriken Throw"] = 10
        if self.lvl >= 10:
            arr_of_skills["Night Attack"] = 50
        if self.lvl >= 50:
            arr_of_skills["Triple Throw"] = 100
        if self.lvl >= 100:
            arr_of_skills["Showdown Challenge"] = 150
        return arr_of_skills

    def Character_Info(self):
        super().Character_Info()
        if not self.is_occupied():
            print(f"character skills: {list(self.skills)}\n")

    def got_exp(self, exp_got):
        super().got_exp(exp_got)
        self.skills = self.add_skill()


class Magician(JobLess):
    def __init__(self, name):
        super().__init__(name)
        self.skills = self.add_skill()

    def add_skill(self):
        arr_of_skills = {}
        if self.lvl >= 1:
            arr_of_skills["Energy Bolt"] = 10
        if self.lvl >= 10:
            arr_of_skills["Thunder Bolt"] = 50
        if self.lvl >= 50:
            arr_of_skills["Ice Strike"] = 100
        if self.lvl >= 100:
            arr_of_skills["Chain Lightning"] = 150

        return arr_of_skills

    def Character_Info(self):
        super().Character_Info()
        if not self.is_occupied():
            print(f"character skills: {list(self.skills)}\n")

    def got_exp(self, exp_got):
        super().got_exp(exp_got)
        self.skills = self.add_skill()


class Archer(JobLess):
    def __init__(self, name):
        super().__init__(name)
        self.skills = self.add_skill()

    def add_skill(self):
        arr_of_skills = {}
        if self.lvl >= 1:
            arr_of_skills["Arrow Blow"] = 10
        if self.lvl >= 10:
            arr_of_skills["Retreat Shot"] = 50
        if self.lvl >= 50:
            arr_of_skills["Hurricane"] = 100
        if self.lvl >= 100:
            arr_of_skills["Uncountable Arrows"] = 150

        return arr_of_skills

    def Character_Info(self):
        super().Character_Info()
        if not self.is_occupied():
            print(f"character skills: {list(self.skills)}\n")

    def got_exp(self, exp_got):
        super().got_exp(exp_got)
        self.skills = self.add_skill()
