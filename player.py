class Player:
    def __init__(self):
        self.gestures = []
        self.name = ""
        self.chosen_gesture = ""
        self.score = 0
        self.populate_gestures()

    def populate_gestures(self):
        self.gestures.append("0 - Rock")
        self.gestures.append("1 - Paper")
        self.gestures.append("2 - Scissors")
        self.gestures.append("3 - Lizard")
        self.gestures.append("4 - Spock")

    def select_choice(self):
        print(self.gestures)
        attack_choice = input("Select a move")
        self.chosen_gesture += attack_choice

    def choose_name(self):
        choice = input("what would you like your name to be?")
        self.name = choice

    def person_or_computer(self):
        poc_choice = input("Would you like to battle a computer or player?")
        if poc_choice == "computer":
            print("The computer will win!")
        else:
            print("May the best man win!")
