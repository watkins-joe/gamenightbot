class Player:

    def __init__(self, name):
        self.name = name
        self.wins = 0

    def __str__(self) -> str:
        return f'Player: {self.name} | Wins: {self.wins}'

    def increaseWins(self):
        self.wins += 1

    def decreaseWins(self):
        self.wins -= 1
