"""Data structure and associated class for keeping track of the player rotation."""


class PlayerNode:
    """A player in the `PlayerRotation` class."""

    def __init__(self, name):
        self.name = name
        self.next = None

    def __repr__(self):
        return f"Player: {self.name}"


class PlayerRotation:
    """Singly linked list of `PlayerNodes` with each player pointing to the next in the rotation.

    Args:
        `players`: A `list` of `PlayerNodes`.
    """

    def __init__(self):
        self.head = None

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

    def add_player(self, player):
        """Adds a new player to the `PlayerRotation` list. The new player is added at the end of the list.

        Args:
            `player`: A `PlayerNode` instance
        """

        # Rotation is empty
        if self.head is None:
            self.head = player
            return

        # Rotation has at least one player, loop thru players to add new player as the new last player.
        current_player = self.head
        while current_player.next:
            current_player = current_player.next

        current_player.next = player

    def remove_player(self, player_name):
        """Removes a player from the `PlayerRotation` list. 

        The algorithm changes the `next` pointer of the player before the `player_name` to be removed to point to the player following the `player_name` to be removed.

        Args:
            `player_name`: The name of the player to be removed as a `string`

        Raises:
            `ValueError`: If the `player` name is not found in the rotation.
        """

        current_player = self.head
        while current_player.next:
            if current_player.next.name == player_name:
                current_player.next = current_player.next.next
                return
            current_player = current_player.next

        raise ValueError(
            f"Player name '{player_name}' not found in rotation.")

    def get_order(self):
        """Returns a human-readable representation of the `PlayerRotation` as a `string`.

        Example: `playerA > playerB > playerC`
        """

        return " > ".join([player.name for player in self])


# Debugging

rotation = PlayerRotation()

rotation.add_player(PlayerNode('meme'))
print(rotation.get_order())      # meme
rotation.add_player(PlayerNode('Askar'))
print(rotation.get_order())      # meme > Askar
rotation.add_player(PlayerNode('4mMan'))
print(rotation.get_order())      # meme > Askar > 4mMan
rotation.add_player(PlayerNode('Greenkid'))
print(rotation.get_order())      # meme > Askar > 4mMan > Greenkid

# print(player_order)

# Debug, ensure linked list is setup properly
# for player in rotation:
#     print(f"{player} points to {player.next}")

# rotation.add_player(PlayerNode('test'))
# order_before = rotation.get_order()     # meme > Askar > 4mMan > Greenkid > test
# print(order_before)
# rotation.remove_player('TEST')
# order_after = rotation.get_order()      # meme > 4mMan > Greenkid > test
# print(order_after)
