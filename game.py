from player import Player


class Game:
    def __init__(self):
        self.player_one = Player()
        self.player_two = Player()

    def run_game(self):
        self.player_one.choose_name()
        self.player_one.person_or_computer()
        player_choice = self.player_one.select_choice()
        enemy_choice = self.player_two.select_choice()
        self.battle(player_choice, enemy_choice)

    def battle(self, player_choice, opponent_choice):
        self.player_one.chosen_gesture = player_choice
        self.player_two.chosen_gesture = opponent_choice
        if player_choice == "Rock" and opponent_choice == "Scissors":
            print(f'Rock crushes Scissors! \n {self.player_one.name} wins!')
            self.player_one.score += 1
        elif player_choice == "Rock" and opponent_choice == "Lizard":
            print(f'Rock crushes Lizard! \n {self.player_one.name} wins!')
            self.player_one.score += 1
        elif player_choice == "Paper" and opponent_choice == "Rock":
            print(f'Paper covers Rock! \n {self.player_one.name} wins!')
            self.player_one.score += 1
        elif player_choice == "Paper" and opponent_choice == "Spock":
            print(f'Paper disproves Spock! \n {self.player_one.name} wins!')
            self.player_one.score += 1
        elif player_choice == "Scissors" and opponent_choice == "Paper":
            print(f'Scissors cut Paper! \n {self.player_one.name} wins!')
            self.player_one.score += 1
        elif player_choice == "Scissors" and opponent_choice == "Lizard":
            print(f'Scissors decapitates Lizard \n {self.player_one.name} wins!')
            self.player_one.score += 1
        elif player_choice == "Lizard" and opponent_choice == "Spock":
            print(f'Lizard poisons Spock \n {self.player_one.name} wins!')
            self.player_one.score += 1
        elif player_choice == "Lizard" and opponent_choice == "Paper":
            print(f'Lizard eats paper \n {self.player_one.name} wins!')
            self.player_one.score += 1
        elif player_choice == "Lizard" and opponent_choice == "Spock":
            print(f'Lizard poisons Spock \n {self.player_one.name} wins!')
            self.player_one.score += 1
        # break for separation of players
        if opponent_choice == "Rock" and player_choice == "Scissors":
            print(f'Rock crushes Scissors! \n {self.player_two.name} wins!')
            self.player_two.score += 1
        elif opponent_choice == "Rock" and player_choice == "Lizard":
            print(f'Rock crushes Lizard! \n {self.player_two.name} wins!')
            self.player_two.score += 1
        elif opponent_choice == "Paper" and player_choice == "Rock":
            print(f'Paper covers Rock! \n {self.player_two.name} wins!')
            self.player_two.score += 1
        elif opponent_choice == "Paper" and player_choice == "Spock":
            print(f'Paper disproves Spock! \n {self.player_two.name} wins!')
            self.player_two.score += 1
        elif opponent_choice == "Scissors" and player_choice == "Paper":
            print(f'Scissors cut Paper! \n {self.player_two.name} wins!')
            self.player_two.score += 1
        elif opponent_choice == "Scissors" and player_choice == "Lizard":
            print(f'Scissors decapitates Lizard \n {self.player_two.name} wins!')
            self.player_two.score += 1
        elif opponent_choice == "Lizard" and player_choice == "Spock":
            print(f'Lizard poisons Spock \n {self.player_two.name} wins!')
            self.player_two.score += 1
        elif opponent_choice == "Lizard" and player_choice == "Paper":
            print(f'Lizard eats paper \n {self.player_two.name} wins!')
            self.player_two.score += 1
        elif opponent_choice == "Lizard" and player_choice == "Spock":
            print(f'Lizard poisons Spock \n {self.player_two.name} wins!')
            self.player_two.score += 1
