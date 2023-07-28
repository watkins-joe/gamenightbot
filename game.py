class Game:

    def __init__(self, name, max_players, early_start):
        self.name = name
        self.max_players = max_players
        self.early_start = early_start

    def __repr__(self):
        return f"{self.name} | Max players: {self.max_players} | Early start?: {self.early_start}"
