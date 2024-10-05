import random
import time  # модуль для задержки


class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        damage = random.randint(1, self.attack_power)
        other.health -= damage
        print(f"{self.name} атаковал {other.name} на {damage} урона!")
        time.sleep(0.9)  # Задержка после атаки

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self, player_name):
        self.player = Hero(player_name)
        self.computer = Hero("Компьютер")

    def start(self):
        print(f"Начинается битва между {self.player.name} и {self.computer.name}!")
        time.sleep(0.9)  # Задержка перед началом боя

        while self.player.is_alive() and self.computer.is_alive():
            self.player.attack(self.computer)
            if not self.computer.is_alive():
                print(f"{self.computer.name} погиб!")
                break

            self.computer.attack(self.player)
            if not self.player.is_alive():
                print(f"{self.player.name} погиб!")
                break

            print(f"У {self.player.name} осталось {self.player.health} здоровья.")
            print(f"У {self.computer.name} осталось {self.computer.health} здоровья.\n")
            time.sleep(0.9)  # Задержка перед следующим раундом

        if self.player.is_alive():
            print(f"{self.player.name} победил!")
        else:
            print(f"{self.computer.name} победил!")


# Запуск игры
if __name__ == "__main__":
    player_name = input("Введите имя вашего героя: ")
    game = Game(player_name)
    game.start()
