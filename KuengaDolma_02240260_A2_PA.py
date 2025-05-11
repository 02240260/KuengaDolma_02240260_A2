import random
from KuengaDolma_02240260_A2_PB import PokemonCardBinder  # Link Part B class here


# Score Tracker Class

class ScoreManager:
    def __init__(self):
        self.guess_number_score = 0
        self.rps_score = 0               #rps = rockpaperscissors
        self.trivia_score = 0
        self.pokemon_score = 0

    def total_score(self):
        return self.guess_number_score + self.rps_score + self.trivia_score + self.pokemon_score


# Guess the Number Game

class GuessNumberGame:
    def __init__(self, score_manager):
        self.score_manager = score_manager

    def play(self):
        print("\nWelcome to the Guess the Number Game!")
        number = random.randint(1, 24)
        attempts = 0
        while True:
            try:
                guess = int(input("Guess a number between 1 and 24: "))
                attempts += 1
                if guess == number:
                    print("Correct! You guessed the correct number.")
                    score = max(5 - attempts, 0)
                    self.score_manager.guess_number_score += score
                    print(f"Score for this game: {score}")
                    break
                elif guess < number:
                    print("Too low!")
                else:
                    print("Too high!")
            except ValueError:
                print("Invalid input. Please enter a number.")


# Rock Paper Scissors Game

class RockPaperScissors:
    def __init__(self, score_manager):
        self.score_manager = score_manager

    def play(self):
        print("\nWelcome to Rock Paper Scissors!")
        choices = ["rock", "paper", "scissors"]
        wins = 0
        rounds = 3

        for i in range(rounds):
            print(f"\nRound {i + 1}:")
            user = input("Choose rock, paper, or scissors: ").lower().strip()
            if user not in choices:
                print("Invalid choice! Round lost.")
                continue
            computer = random.choice(choices)
            print(f"Computer chose: {computer}")

            if user == computer:
                print("It's a tie!")
            elif (user == "rock" and computer == "scissors") or \
                 (user == "scissors" and computer == "paper") or \
                 (user == "paper" and computer == "rock"):
                print("You win this round!")
                wins += 1
            else:
                print("You lose this round!")

        self.score_manager.rps_score += wins
        print(f"You won {wins} round(s). Score added: {wins}")


# Class for Trivia Game

class TriviaGame:
    def __init__(self, score_manager):
        self.score_manager = score_manager
        self.questions = {
            "Science": {
                "Which of these is NOT a planet in our solar system?": "a",
                "What force pulls objects toward the Earth?": "b"
            },
            "Geography": {
                "What is the capital of Tuvalu?": "c",
                "Which country has the most natural lakes in the world?": "a"
            }
        }
        self.options = {
            "Which of these is NOT a planet in our solar system?": ["a) Titan", "b) Earth", "c) Pluto", "d) Mars"],
            "What force pulls objects toward the Earth?": ["a) Friction", "b) Gravity", "c) Magnetism", "d) Electroststic"],
            "What is the capital of Tuvalu?": ["a) Vaduz", "b) Madrid", "c) Funafuti", "d) Rome"],
            "Which country has the most natural lakes in the world?": ["a) Canada", "b) USA", "c) Brazil", "d) China"]
        }

    def play(self):
        print("\nWelcome to Trivia Pursuit!")
        score = 0
        for category, q_set in self.questions.items():
            print(f"\nCategory: {category}")
            for question, correct_answer in q_set.items():
                print(question)
                for opt in self.options[question]:
                    print(opt)
                answer = input("Enter your answer (a/b/c/d): ").lower()
                if answer == correct_answer:
                    print("Correct!")
                    score += 1
                else:
                    print(f"Wrong! The correct answer was: {correct_answer}")
        print(f"You got {score} correct answers.")
        self.score_manager.trivia_score += score


# Class to use PokemonCardBinder from Part B

class PokemonCardBinderGame:
    def __init__(self, score_manager):
        self.binder = PokemonCardBinder()
        self.score_manager = score_manager

    def play(self):
        while True:
            print("\nWelcome to Pokemon Card Binder Manager!")
            print("1. Add Pokemon card")
            print("2. Reset binder")
            print("3. View current placements")
            print("4. Exit")
            choice = input("Select option: ").strip()
            if choice == "1":
                try:
                    number = int(input("Enter Pokedex number: "))
                    self.binder.add_card(number)
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            elif choice == "2":
                self.binder.reset_binder()
            elif choice == "3":
                self.binder.view_binder()
            elif choice == "4":
                self.score_manager.pokemon_score = self.binder.card_count()
                print("Thank you for using Pokemon Card Binder Manager!")
                break
            else:
                print("Invalid option. Please try again.")


# Main Program Menu

class MainProgram:
    def __init__(self):
        self.score_manager = ScoreManager()
        self.games = {
            "1": GuessNumberGame(self.score_manager),
            "2": RockPaperScissors(self.score_manager),
            "3": TriviaGame(self.score_manager),
            "4": PokemonCardBinderGame(self.score_manager)
        }

    def display_menu(self):
        print("\nSelect a function (0-5):")
        print("1. Guess Number Game")
        print("2. Rock Paper Scissors Game")
        print("3. Trivia Pursuit Game")
        print("4. Pokemon Card Binder Manager")
        print("5. Check Current Overall Score")
        print("0. Exit Program")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ").strip()
            if choice == "0":
                print("That's the wrap! Thanks for joining!")
                break
            elif choice in self.games:
                self.games[choice].play()
            elif choice == "5":
                print(f"\nOverall Score:")
                print(f"Guess Number Score: {self.score_manager.guess_number_score}")
                print(f"Rock Paper Scissors Score: {self.score_manager.rps_score}")
                print(f"Trivia Game Score: {self.score_manager.trivia_score}")
                print(f"Pokemon Cards Added: {self.score_manager.pokemon_score}")
                print(f"Total Score: {self.score_manager.total_score()}")
            else:
                print("Invalid choice. Please try again.")


# Start the Program

if __name__ == "__main__":
    program = MainProgram()
    program.run()
