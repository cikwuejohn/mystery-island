connections = {
    "Beach": ["Jungle"],
    "Jungle": ["Beach", "Cave"],
    "Cave": ["Jungle", "Old Bridge"],
    "Old Bridge": ["Cave", "Lighthouse"],
    "Lighthouse": ["Old Bridge"]
}

location_items = {
    "Jungle": "rope",
    "Cave": "lantern"
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

def collect_item(player, item):
    if item not in player["inventory"]:
        player["inventory"].append(item)
        return f"You found a {item}!"

    return f"You already have the {item}."

def explore_location(player):
    location = player["location"]

    print(f"You are now at the {location}.")

    if location in location_items:
        item = location_items[location]
        print(collect_item(player, item))
    else:
        print("There is nothing useful to collect here.")

player = {
    "name": "Ada",
    "location": "Jungle",
    "energy": 5,
    "inventory": [],
    "game_over": False,
    "won": False
}

explore_location(player)
print(player["inventory"])

explore_location(player)
print(player["inventory"])

player = {
    "name": "Ada",
    "location": "Jungle",
    "energy": 5,
    "inventory": [],
    "game_over": False,
    "won": False
}

print(collect_item(player, "rope"))
print(player["inventory"])

print(collect_item(player, "rope"))
print(player["inventory"])