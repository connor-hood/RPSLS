class Player:
    def __init__(self):
        self.gestures = []
        self.name = ""
        self.chosen_gesture = ""
        self.score = 0
        self.populate_gestures()

    def populate_gestures(self):
        self.gestures.append("Rock")
        self.gestures.append("Paper")
        self.gestures.append("Scissors")
        self.gestures.append("Lizard")
        self.gestures.append("Spock")

    def select_choice(self):
        print(self.gestures)
        attack_choice = input("Select a move")
        self.chosen_gesture = attack_choice

    def choose_name(self):
        choice = input("What's your name?")
        self.name = choice

    def person_or_computer(self):
        poc_choice = input("Would you like to battle a computer or player?")
        if poc_choice == "computer":
            print("The computer will win!")
        else:
            print("May the best man win!")
        return poc_choice
