from player import Player


class human(Player):
    def __init__(self):
        super().__init__()

    def select_choice(self):
        print(self.gestures)
        attack_choice = input("Select a move")
        self.chosen_gesture += attack_choice
