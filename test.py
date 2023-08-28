# Debugging

from player_rotation import PlayerNode, PlayerRotation

# Player rotation testing

rotation = PlayerRotation()

rotation.add_player(PlayerNode('meme'))
print(rotation.get_order())      # meme
rotation.add_player(PlayerNode('Askar'))
print(rotation.get_order())      # meme > Askar
rotation.add_player(PlayerNode('4mMan'))
print(rotation.get_order())      # meme > Askar > 4mMan
rotation.add_player(PlayerNode('Greenkid'))
print(rotation.get_order())      # meme > Askar > 4mMan > Greenkid

# Testing removal

# rotation.remove_player("Askar")
print(rotation.get_order())      # meme > 4mMan > Greenkid
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

# Updating leaderboard testing

# Using dict

# Players in the rotation are added to the leaderboard dict automatically, as it's assumed that they will be present more often than not since they have volunteered to host

leaderboard = {
    'A': 1,
    'B': 3,
    'C': 5
}

# Assign player names to wins

for player in rotation:
    leaderboard[player.name] = 1

print(leaderboard)

# Sort players in dict by their wins

sorted_players = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)
sorted_leaderboard = dict(sorted_players)

print(sorted_leaderboard)

leaderboard_string = ""

for player in sorted_leaderboard:
    if sorted_leaderboard[player] > 0:
        leaderboard_string += f"{player}: {sorted_leaderboard[player]}\n"

print(leaderboard_string)
