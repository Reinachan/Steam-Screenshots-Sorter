import requests
from requests_html import HTMLSession

from lib.stored_names import create_stored_name, get_stored_name
from lib.util.format_filename import format_filename
from lib.util.format_title import format_title


def get_game(game_id) -> tuple[str, str]:
    url = f"https://store.steampowered.com/app/{game_id}"

    existing_entry = get_stored_name(game_id)

    if existing_entry:
        return existing_entry
    else:
        try:
            print("getting game title ...")

            session = HTMLSession()
            response = session.get(url)

            title = response.html.find("title")

            title = title[0].text

            title = format_title(title)

            title_filename = format_filename(title)

            create_stored_name(game_id, title, title_filename)

            return title_filename, title

        except requests.exceptions.RequestException as e:
            print(e)
