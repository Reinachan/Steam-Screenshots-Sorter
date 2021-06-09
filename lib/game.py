from lib.game_names import get_game
from lib.sort_to_folders import img_sort
from lib.util.filename_id import get_id


class Game:
    def __init__(self, path):
        self.path = path
        self.game_id = get_id(path)
        self.name = str
        self.folder = str

        self.title()
        self.move_to_folder()

    def title(self) -> None:
        if self.game_id:
            game_title = get_game(self.game_id)
            self.name, self.folder = game_title

            if self.name == "Site Error":
                self.name, self.folder = "Unknown", "Unknown"
        else:
            self.name, self.folder = "Unknown", "Unknown"

        print(self.name)

    def move_to_folder(self) -> None:
        img_sort(self.folder, self.path)
