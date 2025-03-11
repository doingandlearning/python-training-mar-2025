player_dict = {
    "Ludovic": 1,
    "Serge": 4,
    "Lina": -1,
    "Fabian": 2
}


players = list(player_dict.items())
# players.sort(key=lambda p:p[1])


print(sorted(players, key=lambda p:p[1]))  # Functional Programming
print(players)

# Pure Functions
# - Not impact anything beyond themselves ...
