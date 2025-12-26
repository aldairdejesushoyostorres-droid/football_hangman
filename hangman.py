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
        print("\nYou need to guesss this football team:\n")
        for i in self.team:
            if i == " ":
                print(" ", end = " ")
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
            print("You have not made any guesses yet")
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
                if letter in {"1", "2", "3", "4", "5", "6", "7", "8", "9", "0"}:
                    print("\nYou have introduced a number but it should be a letter of the alphabet. Try again!")
                elif letter in self.guesses:
                    print("\nYou have already selected that letter before! Try another one!")
                else:
                    print(f"\nYou have successfully selected the letter {letter}")
                    break
        return letter
    
    def process_guess(self, letter):
        self.guesses.append(letter)
        if letter not in self.team:
            self.count +=1
            print("\nSorry, your guess was wrong!")
        else:
            print("\nGreat! You have guessed a letter of the word correctly!")
    
    def check_victory(self):
        flag = True
        for i in self.team:
            if i not in self.guesses:
                flag = False
                break
        return flag
    
    def guess_word(self):
        word = input("So... You want to guess the word, huh! Go ahead: ")
        return True if word == self.team else False

    def game_over(self):
        return True if self.count >= self.max_errors else False