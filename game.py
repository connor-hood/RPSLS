from player import Player

class Game:
    def __init__(self):
        self.player_one = Player()
        self.player_two = Player()

    def run_game(self):
        self.player_one.choose_name()
        self.player_one.person_or_computer()
        self.player_one.select_choice()


    def battle(self, player_choice, opponent_choice):
        self.player_one.chosen_gesture = player_choice
        self.player_two.chosen_gesture = opponent_choice
        if player_choice == 0 and opponent_choice == 2:
            print("Rock crushes Scissors!")
            self.player_one.score += 1
        elif player_choice == 0 and opponent_choice == 3:
            print("Rock crushes Lizard!")
            self.player_one.score += 1
        elif player_choice == 1 and opponent_choice == 0:
            print("Paper covers Rock!")
            self.player_one.score += 1
        elif player_choice == 1 and opponent_choice == 4:
            print("Paper disproves Spock!")
            self.player_one.score += 1
        elif player_choice == 2 and opponent_choice == 1:
            print("Scissors cut Paper!")
            self.player_one.score += 1
        elif player_choice == 2 and opponent_choice == 3:
            print("Scissors decapitates Lizard")
            self.player_one.score += 1
        elif player_choice == 3 and opponent_choice == 4:
            print("Lizard poisons Spock")
            self.player_one.score += 1
        elif player_choice == 3 and opponent_choice == 1:
            print("Lizard eats paper")
            self.player_one.score += 1
        elif player_choice == 3 and opponent_choice == 4:
            print("Lizard poisons Spock")
            self.player_one.score += 1




