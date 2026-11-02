connections = {
    "Beach": ["Jungle"],
    "Jungle": ["Beach", "Cave"],
    "Cave": ["Jungle", "Old Bridge"],
    "Old Bridge": ["Cave", "Lighthouse"],
    "Lighthouse": ["Old Bridge"]
}

def move_player(player, destination):
    current_location = player["location"]

    if destination in connections[current_location]:
        player["location"] = destination
        player["energy"] -= 1
        return "Move successful!"

    return "You cannot travel there."

player = {
    "name": "Ada",
    "location": "Beach",
    "energy": 5,
    "inventory": [],
    "game_over": False,
    "won": False
}

print(move_player(player, "Jungle"))
print(player)

print(move_player(player, "Lighthouse"))
print(player)