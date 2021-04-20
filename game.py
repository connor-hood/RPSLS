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
            print(f'Rock crushes Scissors! \n {self.player_one.name} wins!')
            self.player_one.score += 1
        elif player_choice == 0 and opponent_choice == 3:
            print(f'Rock crushes Lizard! \n {self.player_one.name} wins!')
            self.player_one.score += 1
        elif player_choice == 1 and opponent_choice == 0:
            print(f'Paper covers Rock! \n {self.player_one.name} wins!')
            self.player_one.score += 1
        elif player_choice == 1 and opponent_choice == 4:
            print(f'Paper disproves Spock! \n {self.player_one.name} wins!')
            self.player_one.score += 1
        elif player_choice == 2 and opponent_choice == 1:
            print(f'Scissors cut Paper! \n {self.player_one.name} wins!')
            self.player_one.score += 1
        elif player_choice == 2 and opponent_choice == 3:
            print(f'Scissors decapitates Lizard \n {self.player_one.name} wins!')
            self.player_one.score += 1
        elif player_choice == 3 and opponent_choice == 4:
            print(f'Lizard poisons Spock \n {self.player_one.name} wins!')
            self.player_one.score += 1
        elif player_choice == 3 and opponent_choice == 1:
            print(f'Lizard eats paper \n {self.player_one.name} wins!')
            self.player_one.score += 1
        elif player_choice == 3 and opponent_choice == 4:
            print(f'Lizard poisons Spock \n {self.player_one.name} wins!')
            self.player_one.score += 1
        # break for separation of players
        if opponent_choice == 0 and player_choice == 2:
            print(f'Rock crushes Scissors! \n {self.player_two.name} wins!')
            self.player_two.score += 1
        elif opponent_choice == 0 and player_choice == 3:
            print(f'Rock crushes Lizard! \n {self.player_two.name} wins!')
            self.player_two.score += 1
        elif opponent_choice == 1 and player_choice == 0:
            print(f'Paper covers Rock! \n {self.player_two.name} wins!')
            self.player_two.score += 1
        elif opponent_choice == 1 and player_choice == 4:
            print(f'Paper disproves Spock! \n {self.player_two.name} wins!')
            self.player_two.score += 1
        elif opponent_choice == 2 and player_choice == 1:
            print(f'Scissors cut Paper! \n {self.player_two.name} wins!')
            self.player_two.score += 1
        elif opponent_choice == 2 and player_choice == 3:
            print(f'Scissors decapitates Lizard \n {self.player_two.name} wins!')
            self.player_two.score += 1
        elif opponent_choice == 3 and player_choice == 4:
            print(f'Lizard poisons Spock \n {self.player_two.name} wins!')
            self.player_two.score += 1
        elif opponent_choice == 3 and player_choice == 1:
            print(f'Lizard eats paper \n {self.player_two.name} wins!')
            self.player_two.score += 1
        elif opponent_choice == 3 and player_choice == 4:
            print(f'Lizard poisons Spock \n {self.player_two.name} wins!')
            self.player_two.score += 1