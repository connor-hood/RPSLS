from player import Player
import random


class Computer(Player):
    def __init__(self):
        super().__init__()
        self.name = "Computer"

    def select_choice(self):
        print(self.gestures)
        attack_choice = random.choice(self.gestures)
        self.chosen_gesture = attack_choice
        return self.chosen_gesture
