from player import Player

class Game:
    def __init__(self):
        self.player_one = Player()
        self.player_two = Player()

    def run_game(self):
        self.player_one.choose_name()
        self.player_one.select_choice()
        self.player_one.person_or_computer()


