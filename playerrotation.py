"""Data structure for keeping track of the player rotation. Implemented with a singly linked list."""


class PlayerNode:
    """A player in the PlayerRotation class."""

    def __init__(self, name):
        self.name = name
        self.next = None

    def __repr__(self):
        return f"Player: {self.name}"


class PlayerRotation:
    def __init__(self, players=None):
        self.head = None
        if players:
            # removes first Player from {players} list, assigning it to head
            self.head = players.pop(0)

        currentPlayer = self.head
        if currentPlayer:
            for player in players:
                currentPlayer.next = player
                currentPlayer = player

    def __iter__(self):
        player = self.head
        while player:
            yield player
            player = player.next

    def __repr__(self):
        player = self.head

        player_names = []
        while player:
            player_names.append(player.name)
            player = player.next
        return " > ".join(player_names)

    def get_order(self):
        """Returns a human-readable representation of the `PlayerRotation` as a `string`.

        Example: `playerA > playerB > playerC`

        """
        return " > ".join([player.name for player in self])


players = [PlayerNode('meme'), PlayerNode('Askar'),
           PlayerNode('4mMan'), PlayerNode('Greenkid')]

rotation = PlayerRotation(players)

player_order = rotation.get_order()

print(player_order)

# Debug, ensure linked list is setup properly
for player in rotation:
    print(f"{player} points to {player.next}")
