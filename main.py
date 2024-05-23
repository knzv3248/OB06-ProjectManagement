"""
Классы:
Класс Hero:
    Атрибуты:
    Имя (name)
    Здоровье (health), начальное значение 100
    Сила удара (attack_power), начальное значение 20

    Методы:
    attack(other): атакует другого героя (other), отнимая здоровье в размере своей силы удара
    is_alive(): возвращает True, если здоровье героя больше 0, иначе False
Класс Game:
    Атрибуты:
    Игрок (player), экземпляр класса Hero
    Компьютер (computer), экземпляр класса Hero

    Методы:
    start(): начинает игру, чередует ходы игрока и компьютера, пока один из героев не умрет. Выводит информацию о каждом ходе (кто атаковал и сколько здоровья осталось у противника) и объявляет победителя.
"""

import random

class Hero():
    def __init__(self, health=100, attack_power=20, win=0):
        self.health = health
        self.attack_power = attack_power
        self.win = win
    def attack(self, other):
        other.health -= self.attack_power

    def is_alive(self):
        return self.health > 0

class Game():
    def __init__(self):
        self.player = Hero()
        self.computer = Hero()

    def start(self):
        print("Игра между игроком и компьютером начинается. Игра состоит из 5 раундов.\n"
              "Победитель будет определён по максимальному числу побед.")
        input("Для начала игры нажмите любую клавишу.\n"
              "Соперник, начинающий бой, будет выбран случайным образом.")
        print("Игра началась.")

        for i in range(1, 6):
            if rand(0, 1) == 0:
                fighter, other = "Игрок", "Компьютер"
            else:
                fighter, other = "Компьютер", "Игрок"

            while game.player.is_alive() and game.computer.is_alive():

                if fighter == 'Игрок':
                    game.player.attack(game.computer)
                    print(f"Раунд {i}. Атакует '{fighter}', у соперника '{other}' осталось здоровья {game.computer.health}")
                    fighter, other = "Компьютер", "Игрок"
                else:
                    game.computer.attack(game.player)
                    print(f"Раунд {i}. Атакует '{fighter}', у соперника '{other}' осталось здоровья {game.player.health}")
                    fighter, other = "Игрок", "Компьютер"

            if game.player.is_alive():
                print(f"В раунде {i} победил 'Игрок'")
                game.player.win += 1
            else:
                print(f"В раунде {i} победил 'Компьютер'")
                game.computer.win += 1
            print(f"Счёт в матче \n'Игрок' ({game.player.win}) : 'Компьютер' ({game.computer.win})")
            game.player.health = 100
            game.computer.health = 100

        if game.player.win > game.computer.win:
            print(f"Со счётом {game.player.win} : {game.computer.win} победил 'Игрок'")
        else:
            print(f"Со счётом {game.computer.win} : {game.player.win} победил 'Компьютер'")



def rand(n_min, n_max):
    return random.randint(n_min, n_max)

game = Game()
game.start()

