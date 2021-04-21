from player import Player
from computer import Computer


class Game:
    def __init__(self):
        self.player_one = Player()
        self.player_two = ''

    def run_game(self):
        self.display_welcome()
        self.player_one.choose_name()
        choice = self.player_one.person_or_computer()
        if choice == "computer":
            self.player_two = Computer()
        else:
            self.player_two = Player()
            self.player_two.choose_name()
        self.score_counter()

    def battle(self):
        player_choice = self.player_one.select_choice()
        opponent_choice = self.player_two.select_choice()
        if self.player_one.chosen_gesture == self.player_two.chosen_gesture:
            print(f"It's a tie! \n Score: {self.player_one.name}: {self.player_one.score}, {self.player_two.name}: {self.player_two.score}")
        elif self.player_one.chosen_gesture == "Rock" and self.player_two.chosen_gesture == "Scissors":
            print(f'Rock crushes Scissors! \n{self.player_one.name} wins!')
            self.player_one.score += 1
            print(
                f'Score: {self.player_one.name}: {self.player_one.score}, {self.player_two.name}: {self.player_two.score}')
        elif self.player_one.chosen_gesture == "Rock" and self.player_two.chosen_gesture == "Lizard":
            print(f'Rock crushes Lizard! \n{self.player_one.name} wins!')
            self.player_one.score += 1
            print(
                f'Score: {self.player_one.name}: {self.player_one.score}, {self.player_two.name}: {self.player_two.score}')
        elif self.player_one.chosen_gesture == "Paper" and self.player_two.chosen_gesture == "Rock":
            print(f'Paper covers Rock! \n{self.player_one.name} wins!')
            self.player_one.score += 1
            print(
                f'Score: {self.player_one.name}: {self.player_one.score}, {self.player_two.name}: {self.player_two.score}')
        elif self.player_one.chosen_gesture == "Paper" and self.player_two.chosen_gesture == "Spock":
            print(f'Paper disproves Spock! \n{self.player_one.name} wins!')
            self.player_one.score += 1
            print(
                f'Score: {self.player_one.name}: {self.player_one.score}, {self.player_two.name}: {self.player_two.score}')
        elif self.player_one.chosen_gesture == "Scissors" and self.player_two.chosen_gesture == "Paper":
            print(f'Scissors cut Paper! \n{self.player_one.name} wins!')
            self.player_one.score += 1
            print(
                f'Score: {self.player_one.name}: {self.player_one.score}, {self.player_two.name}: {self.player_two.score}')
        elif self.player_one.chosen_gesture == "Scissors" and self.player_two.chosen_gesture == "Lizard":
            print(f'Scissors decapitates Lizard \n{self.player_one.name} wins!')
            self.player_one.score += 1
            print(
                f'Score: {self.player_one.name}: {self.player_one.score}, {self.player_two.name}: {self.player_two.score}')
        elif self.player_one.chosen_gesture == "Lizard" and self.player_two.chosen_gesture == "Paper":
            print(f'Lizard eats paper \n{self.player_one.name} wins!')
            self.player_one.score += 1
            print(
                f'Score: {self.player_one.name}: {self.player_one.score}, {self.player_two.name}: {self.player_two.score}')
        elif self.player_one.chosen_gesture == "Lizard" and self.player_two.chosen_gesture == "Spock":
            print(f'Lizard poisons Spock \n{self.player_one.name} wins!')
            self.player_one.score += 1
            print(
                f'Score: {self.player_one.name}: {self.player_one.score}, {self.player_two.name}: {self.player_two.score}')
        elif self.player_one.chosen_gesture == "Spock" and self.player_two.chosen_gesture == "Scissors":
            print(f'Spock smashes Scissors! \n{self.player_one.name} wins!')
            self.player_one.score += 1
            print(
                f'Score: {self.player_one.name}: {self.player_one.score}, {self.player_two.name}: {self.player_two.score}')
        elif self.player_one.chosen_gesture == "Spock" and self.player_two.chosen_gesture == "Rock":
            print(f'Spock vaporizes Rock! \n{self.player_one.name} wins!')
            self.player_one.score += 1
            print(
                f'Score: {self.player_one.name}: {self.player_one.score}, {self.player_two.name}: {self.player_two.score}')
        # break for separation of players
        elif self.player_two.chosen_gesture == "Scissors" and self.player_one.chosen_gesture == "Spock":
            print(f'Spock smashes Scissors! \n{self.player_two.name} wins!')
            self.player_two.score += 1
            print(
                f'Score: {self.player_one.name}: {self.player_one.score}, {self.player_two.name}: {self.player_two.score}')

        elif self.player_two.chosen_gesture == "Rock" and self.player_one.chosen_gesture == "Spock":
            print(f'Spock vaporizes Rock! \n{self.player_two.name} wins!')
            self.player_two.score += 1
            print(
                f'Score: {self.player_one.name}: {self.player_one.score}, {self.player_two.name}: {self.player_two.score}')
        elif self.player_two.chosen_gesture == "Rock" and self.player_one.chosen_gesture == "Scissors":
            print(f'Rock crushes Scissors! \n{self.player_two.name} wins!')
            self.player_two.score += 1
            print(
                f'Score: {self.player_one.name}: {self.player_one.score}, {self.player_two.name}: {self.player_two.score}')
        elif self.player_two.chosen_gesture == "Rock" and self.player_one.chosen_gesture == "Lizard":
            print(f'Rock crushes Lizard! \n{self.player_two.name} wins!')
            self.player_two.score += 1
            print(
                f'Score: {self.player_one.name}: {self.player_one.score}, {self.player_two.name}: {self.player_two.score}')
        elif self.player_two.chosen_gesture == "Paper" and self.player_one.chosen_gesture == "Rock":
            print(f'Paper covers Rock! \n{self.player_two.name} wins!')
            self.player_two.score += 1
            print(
                f'Score: {self.player_one.name}: {self.player_one.score}, {self.player_two.name}: {self.player_two.score}')
        elif self.player_two.chosen_gesture == "Paper" and self.player_one.chosen_gesture == "Spock":
            print(f'Paper disproves Spock! \n{self.player_two.name} wins!')
            self.player_two.score += 1
            print(
                f'Score: {self.player_one.name}: {self.player_one.score}, {self.player_two.name}: {self.player_two.score}')
        elif self.player_two.chosen_gesture == "Scissors" and self.player_one.chosen_gesture == "Paper":
            print(f'Scissors cut Paper! \n{self.player_two.name} wins!')
            self.player_two.score += 1
            print(
                f'Score: {self.player_one.name}: {self.player_one.score}, {self.player_two.name}: {self.player_two.score}')
        elif self.player_two.chosen_gesture == "Scissors" and self.player_one.chosen_gesture == "Lizard":
            print(f'Scissors decapitates Lizard \n{self.player_two.name} wins!')
            self.player_two.score += 1
            print(
                f'Score: {self.player_one.name}: {self.player_one.score}, {self.player_two.name}: {self.player_two.score}')
        elif self.player_two.chosen_gesture == "Lizard" and self.player_one.chosen_gesture == "Spock":
            print(f'Lizard poisons Spock \n{self.player_two.name} wins!')
            self.player_two.score += 1
            print(
                f'Score: {self.player_one.name}: {self.player_one.score}, {self.player_two.name}: {self.player_two.score}')
        elif self.player_two.chosen_gesture == "Lizard" and self.player_one.chosen_gesture == "Paper":
            print(f'Lizard eats paper \n{self.player_two.name} wins!')
            self.player_two.score += 1
            print(
                f'Score: {self.player_one.name}: {self.player_one.score}, {self.player_two.name}: {self.player_two.score}')
        elif self.player_two.chosen_gesture == "Lizard" and self.player_one.chosen_gesture == "Spock":
            print(f'Lizard poisons Spock \n{self.player_two.name} wins!')
            self.player_two.score += 1
            print(
                f'Score: {self.player_one.name}: {self.player_one.score}, {self.player_two.name}: {self.player_two.score}')

    def score_counter(self):
        while self.player_one.score < 3 and self.player_two.score < 3:
            self.battle()
        if self.player_one.score == 3:
            print(f"{self.player_one.name} wins the game!")
        else:
            print(f"{self.player_two.name} wins the game!")

    def display_welcome(self):
        print("Welcome to Rock v Paper v Scissor v Lizard v Spock \n"
              "Best out of three will determine the winner")
