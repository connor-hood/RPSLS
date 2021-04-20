class Player:
    def __init__(self):
        self.gestures = []
        self.name = ""
        self.chosen_gesture = ""
        self.score = 0

    def select_choice(self):
        self.gestures.append("Rock")
        self.gestures.append("Paper")
        self.gestures.append("Scissors")
        self.gestures.append("Lizard")
        self.gestures.append("Spock")
        print(self.gestures)

    def choose_name(self):
        choice = input("what would you like your name to be?")
        self.name = choice
