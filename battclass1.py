
hero = None

class Profile:
    def __init__(self):
        self.name = None
        self.age = None
        self.gender = None

    def set_name(self):
        while True:
            name = input("введите ваше имя:-> ")
            if name.replace(" ", "").isalpha():
                self.name = name
                break
            else:
                print("сначала создайте профиль")

    def set_age(self):
        while True:
            age = input("введите ваш возраст:-> ")
            if age.isdigit():
                age = int(age)
                if 5 <= age <= 80:
                    self.age = age
                    break
                else:
                    print("ошибка ввода возраста")
            else:
                print("ошибка ввода. попробуйте еще раз!")

    def set_gender(self):
        while True:
            print("\n== пол ==")
            print("1. парень")
            print("2. девушка")

            choice = input("выберите ваш пол.-> ")

            if not choice.isdigit():
                print("ошибка ввода. попробуйте еще раз!")
                continue

            choice = int(choice)

            if choice == 1:
                self.gender = "парень"
                break

            elif choice == 2:
                self.gender = "девушка"
                break
            else:
                print("ошибка ввода. попробуйте еще раз!")

    def show_profile(self):
        print(self.name)
        print(self.age)
        print(self.gender)

player = Profile()

class Character:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, enemy):
        enemy.take_damage(self.damage)
        print(f"вы ударили врага, у врага {enemy.hp} хп")

    def take_damage(self, amount):
        self.hp -= amount
        print(f"вас атаковали, у вас {self.hp} хп")

class Mage(Character):
    def __init__(self, name):
        super().__init__(name, hp=80, damage=35)

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, hp=100, damage=20)

class Archer(Character):
    def __init__(self, name):
        super().__init__(name, hp=90, damage=25)

def choose_class(player_name):
    while True:
        print("\n== выбор героя ==")
        print("1. маг (сильный урон, мало хп)")
        print("2. воин (малый урон, много хп)")
        print("3. стрелок (средний баланс)")

        choice = input("выберите героя.-> ")

        if not choice.isdigit():
            print("ошибка ввода. попробуйте еще раз!")
            continue

        choice = int(choice)

        if choice == 1:
            return Mage(player_name)
        
        elif choice == 2:
            return Warrior(player_name)
        
        elif choice == 3:
            return Archer(player_name)
        else:
            print("ошибка ввода.попробуйте еще раз!")

def battle(hero, enemy):
    print(f"вы сражаетесь против {enemy.name}")

    while hero.hp > 0 and enemy.hp > 0:
        input("нажмите - Enter, чтобы атаковать:-> ")

        hero.attack(enemy)

        if enemy.hp <= 0:
            print("вы выиграли")
            break

        enemy.attack(hero)

        if hero.hp <= 0:
            print("вы проиграли")
            break
    

def start_menu():
    while True:
        print("\n== Стартовое меню ==")
        print("1. создать профиль")
        print("2. выбрать героя")
        print("3. главное  меню")
        print("4. выйти из игры")

        choice = input("выберите действие:-> ")

        if not choice.isdigit():
            print("ошибка ввода. попробуйте еще раз!")
            continue

        choice = int(choice)

        if choice == 1:
            player.set_name()
            player.set_age()
            player.set_gender()

        elif choice == 2:
            
            global hero
            if not player.name:
                print("сначала создайте профиль")
            else:
                hero = choose_class(player.name)

        elif choice == 3:
            if not player.name:
                print("сначала создайте профиль")
            else:
                main_menu()

        elif choice == 4:
            print("выйти")
            break
        else:
            print("ошибка ввода. попробуйте еще раз!")

def main_menu():
    while True:
        print("\n== Главное меню ==")
        print("1. профиль")
        print("2. битва")
        print("3. выйти в стартовое меню")

        choice = input("выберите действие:-> ")

        if not choice.isdigit():
            print("ошибка ввода. попробуйте еще раз!")
            continue

        choice = int(choice)

        if choice == 1:
            print(player.name)
            print(player.age)
            print(player.gender)

        elif choice == 2:
            if hero is None:
                print("сначала выберите героя")
            else:
                enemy = Warrior("слизь")
                battle(hero, enemy)

        elif choice == 3:
            print("выйти в стартовое меню")
            break
        else:
            print("ошибка ввода. попробуйте еще раз!")