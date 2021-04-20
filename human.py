from player import Player


class human(Player):
    def __init__(self):
        super().__init__()

    def select_choice(self):
        print(self.gestures)
        attack_choice = int(input("Select a move"))
        while attack_choice is not '0' or '1' or '2' or '3' or '4':
            print("please enter a correct value")
        self.chosen_gesture += attack_choice
        return self.chosen_gesture
