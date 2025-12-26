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
        print(f"\nThe team you're trying to guess is from {self.league}")

    def word_masker(self):
        for i in self.team:
            if i == " ":
                print(" ", end = " ")
            elif i.lower() in self.guesses:
                print(i, end = " ")
            else:
                print("_", end = " ")