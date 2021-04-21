from player import Player


class human(Player):
    def __init__(self):
        super().__init__()

    def select_choice(self):
        print(self.gestures)
        attack_choice = input("Select a move")
        while attack_choice != "Rock" or "Paper" or "Scissors" or "Lizard" or "Spock":
            print("please enter a correct value")
        self.chosen_gesture = attack_choice
        return self.chosen_gesture
