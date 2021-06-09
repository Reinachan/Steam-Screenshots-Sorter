import csv


def get_stored_name(game_id: str):
    # print("get_stored")
    try:
        with open("games_cache.csv", "r") as games_cache:
            # Convert JSON file to Python Types
            obj = csv.DictReader(games_cache)
            for game in obj:
                if game_id in game["id"]:
                    return game["name"], game["filename"]

            return None

    except Exception:
        print("no stored name")
        return None


def create_stored_name(game_id, name, filename):
    fieldnames = ["id", "name", "filename"]

    if filename.startswith(".\\"):
        filename = filename[2:]

    game_storage = {"id": game_id, "name": name, "filename": filename}

    try:
        with open("games_cache.csv", "a+", newline="") as games_cache:
            add_entry = csv.DictWriter(games_cache, fieldnames=fieldnames)
            add_entry.writerow(game_storage)
    except:
        print("error with storing dict in games_cache")
