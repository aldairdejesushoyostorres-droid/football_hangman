import random

class Hangman:
    def __init__(self, max_errors: int) -> None:
        self.max_errors = max_errors
        self.guesses = []
        self.count = 0
        
        # The dictionary is defined locally inside __init__
        word_bank = {
            "England": [
                "Arsenal", "Aston Villa", "Bournemouth", "Brentford", "Brighton", 
                "Chelsea", "Crystal Palace", "Everton", "Fulham", "Ipswich Town", 
                "Leicester City", "Liverpool", "Manchester City", "Manchester United", 
                "Newcastle United", "Nottingham Forest", "Southampton", "Tottenham Hotspur", 
                "West Ham United", "Wolverhampton Wanderers"
            ],
            "Spain": [
                "Alaves", "Athletic Bilbao", "Atletico Madrid", "Barcelona", "Celta Vigo", 
                "Espanyol", "Getafe", "Girona", "Las Palmas", "Leganes", 
                "Mallorca", "Osasuna", "Rayo Vallecano", "Real Betis", "Real Madrid", 
                "Real Sociedad", "Sevilla", "Valencia", "Valladolid", "Villarreal"
            ],
            "France": [
                "Angers", "Auxerre", "Brest", "Le Havre", "Lens", 
                "Lille", "Lyon", "Marseille", "Monaco", "Montpellier", 
                "Nantes", "Nice", "PSG", "Reims", "Rennes", 
                "Saint-Etienne", "Strasbourg", "Toulouse"
            ],
            "Italy": [
                "AC Milan", "Atalanta", "Bologna", "Cagliari", "Como", 
                "Empoli", "Fiorentina", "Genoa", "Inter Milan", "Juventus", 
                "Lazio", "Lecce", "Monza", "Napoli", "Parma", 
                "Roma", "Torino", "Udinese", "Venezia", "Verona"
            ],
            "Germany": [
                "Augsburg", "Bayer Leverkusen", "Bayern Munich", "Bochum", "Borussia Dortmund", 
                "Borussia Monchengladbach", "Eintracht Frankfurt", "Freiburg", "Heidenheim", "Hoffenheim", 
                "Holstein Kiel", "Mainz", "RB Leipzig", "St Pauli", "Stuttgart", 
                "Union Berlin", "Werder Bremen", "Wolfsburg"
            ],
            "Portugal": [
                "Arouca", "AVS", "Benfica", "Boavista", "Braga", 
                "Casa Pia", "Estoril", "Estrela Amadora", "Famalicao", "Farense", 
                "Gil Vicente", "Moreirense", "Nacional", "Porto", "Rio Ave", 
                "Santa Clara", "Sporting CP", "Vitoria Guimaraes"
            ],
            "Netherlands": [
                "Ajax", "Almere City", "AZ Alkmaar", "Feyenoord", "Fortuna Sittard", 
                "Go Ahead Eagles", "Groningen", "Heerenveen", "Heracles Almelo", "NAC Breda", 
                "NEC Nijmegen", "PEC Zwolle", "PSV Eindhoven", "RKC Waalwijk", "Sparta Rotterdam", 
                "Twente", "Utrecht", "Willem II"
            ]
        }

        self.league = random.choice(list(word_bank.keys()))
        self.team = random.choice(word_bank[self.league]).lower()

    def show_hint(self):
        print(f"The team you're trying to guess is from {self.league}!")

    def word_masker(self):
        print("You need to guesss this football team:\n")
        for i in self.team:
            # Reveal if it's a space OR if it's not a letter (like a hyphen)
            if i == " " or not i.isalpha():
                print(i, end = " ")
            elif i.lower() in self.guesses:
                print(i, end = " ")
            else:
                print("_", end = " ")
        print("\n")
    
    def game_status(self):
        self.word_masker()
        self.show_hint()
        print(f"These are your chances left for guessing the team: {self.max_errors - self.count}")
        if len(self.guesses) == 0: 
            pass
        else:
            print("The letters you have used are the following: {", end = "")
            letters = 0
            for i in self.guesses:
                letters += 1
                print(f"{i}, ", end = " ") if letters < len(self.guesses) else print(f"{i}", end = " ")
            print("}")
    
    def user_input(self):
        while True:
            letter = input("\nMake your guess! Give us your letter: ").lower()
            if len(letter) == 0:
                print("\nYou can't give us nothing... Try again but introduce a letter this time!")
            elif len(letter) > 1:
                print("\nYou have to give us a letter and not a word as you just did. Try again!")
            else:
                if letter.isalpha() != True :
                    print("\nYou did not introduce a letter. Try again!")
                elif letter in self.guesses:
                    print("\nYou have already selected that letter before! Try another one!")
                else:
                    break
        return letter

    def process_guess(self, letter):
        self.guesses.append(letter)
        if letter not in self.team:
            self.count += 1
            print("\nSorry, your guess was wrong!\n")
        else:
            print("\nGreat! You have guessed a letter of the team!\n")
    
    def check_victory(self):
        flag = True
        for i in self.team:
            # Skip spaces AND non-letters (like hyphens)
            if i == " " or not i.isalpha():
                pass
            elif i not in self.guesses:
                flag = False
                break
        return flag
    
    def guess_word(self):
        word = input("So... You want to guess the word, huh! Go ahead: ").lower()
        return True if word == self.team else False

    def game_over(self):
        return True if self.count >= self.max_errors else False
    
    def play_game(self):
        print("Welcome to Football Hangman!")
        while True:
            self.game_status()
            try:
                print("\nSelect one of the following options:")
                print("\n1) Guess the word right away")
                print("\n2) Guess a letter")
                option = int(input("\nYour choice: "))
                if option not in {1, 2}:
                    print("\nThere are only two options, you need to pick one of them! Try again!")
                else:
                    if option == 1:
                        risky_guess = self.guess_word()
                        if risky_guess == True:
                            print("You guessed the team correctly! You are THE GOAT!!!!")
                        else:
                            print("There's a high price for taking such a big leap! You did not guess the team correctly.\nYou lost the game, my friend! See you next time!")
                        break
                    else:
                        letter = self.user_input()
                        self.process_guess(letter)
            except ValueError:
                print("\nYou need to introduce a numeric value in order to proceed... Try again!")
            if self.check_victory():
                print(f"\nYou guessed the team! It was {self.team}! Congratulations, you just won!")
                break
            if self.game_over():
                print(f"\nYou ran out of guesses! You just lost the game, my friend! The team was {self.team}")
                break

if __name__ == "__main__":
    player = Hangman(3)
    player.play_game()