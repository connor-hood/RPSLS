class Player:
    def __init__(self):
        self.gestures = []
        self.name = ""
        self.chosen_gesture = ""
        self.score = 0

    def select_choice(self):
        self.gestures.append("0 - Rock")
        self.gestures.append("1 - Paper")
        self.gestures.append("2 - Scissors")
        self.gestures.append("3 - Lizard")
        self.gestures.append("4 - Spock")
        print(self.gestures)
        attack_choice = input("Select a move")
        self.chosen_gesture += attack_choice

    def choose_name(self):
        choice = input("what would you like your name to be?")
        self.name = choice

    def person_or_computer(self):
        print("Would you like to battle a computer or player?")
