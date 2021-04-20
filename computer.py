from player import Player
import random


class Computer(Player):
    super().__init__()

    def select_choice(self):
        print(self.gestures)
        attack_choice = random.choice(self.gestures)
        self.chosen_gesture += attack_choice
        return self.chosen_gesture
