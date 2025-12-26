import random

class Hangman:
    def __init__(self, max_errors: int) -> None:
        self.max_errors = max_errors
        self.guesses = []
        self.count = 0
        
        # The dictionary is defined locally inside __init__
        word_bank = {
            "england": [
                "Arsenal", "Aston Villa", "Bournemouth", "Brentford", "Brighton", 
                "Chelsea", "Crystal Palace", "Everton", "Fulham", "Ipswich Town", 
                "Leicester City", "Liverpool", "Manchester City", "Manchester United", 
                "Newcastle United", "Nottingham Forest", "Southampton", "Tottenham Hotspur", 
                "West Ham United", "Wolverhampton Wanderers"
            ],
            "spain": [
                "Alaves", "Athletic Bilbao", "Atletico Madrid", "Barcelona", "Celta Vigo", 
                "Espanyol", "Getafe", "Girona", "Las Palmas", "Leganes", 
                "Mallorca", "Osasuna", "Rayo Vallecano", "Real Betis", "Real Madrid", 
                "Real Sociedad", "Sevilla", "Valencia", "Valladolid", "Villarreal"
            ],
            "france": [
                "Angers", "Auxerre", "Brest", "Le Havre", "Lens", 
                "Lille", "Lyon", "Marseille", "Monaco", "Montpellier", 
                "Nantes", "Nice", "PSG", "Reims", "Rennes", 
                "Saint-Etienne", "Strasbourg", "Toulouse"
            ],
            "italy": [
                "AC Milan", "Atalanta", "Bologna", "Cagliari", "Como", 
                "Empoli", "Fiorentina", "Genoa", "Inter Milan", "Juventus", 
                "Lazio", "Lecce", "Monza", "Napoli", "Parma", 
                "Roma", "Torino", "Udinese", "Venezia", "Verona"
            ],
            "germany": [
                "Augsburg", "Bayer Leverkusen", "Bayern Munich", "Bochum", "Borussia Dortmund", 
                "Borussia Monchengladbach", "Eintracht Frankfurt", "Freiburg", "Heidenheim", "Hoffenheim", 
                "Holstein Kiel", "Mainz", "RB Leipzig", "St Pauli", "Stuttgart", 
                "Union Berlin", "Werder Bremen", "Wolfsburg"
            ],
            "portugal": [
                "Arouca", "AVS", "Benfica", "Boavista", "Braga", 
                "Casa Pia", "Estoril", "Estrela Amadora", "Famalicao", "Farense", 
                "Gil Vicente", "Moreirense", "Nacional", "Porto", "Rio Ave", 
                "Santa Clara", "Sporting CP", "Vitoria Guimaraes"
            ],
            "netherlands": [
                "Ajax", "Almere City", "AZ Alkmaar", "Feyenoord", "Fortuna Sittard", 
                "Go Ahead Eagles", "Groningen", "Heerenveen", "Heracles Almelo", "NAC Breda", 
                "NEC Nijmegen", "PEC Zwolle", "PSV Eindhoven", "RKC Waalwijk", "Sparta Rotterdam", 
                "Twente", "Utrecht", "Willem II"
            ]
        }