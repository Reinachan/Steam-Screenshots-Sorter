import csv
import os
import sys
import time

from watchdog.events import PatternMatchingEventHandler
from watchdog.observers import Observer

from lib.game import Game
from lib.handle_existing_files import existing_img


class ImageHandler(PatternMatchingEventHandler):
    patterns = ["*.png", "*.jpg", "*.jpeg"]

    def process(self, event):
        """
        event.event_type
            'modified' | 'created' | 'moved' | 'deleted'
        event.is_directory
            True | False
        event.src_path
            path/to/observed/file
        """
        Game(event.src_path[2:])

    def on_created(self, event):
        self.process(event)


if __name__ == "__main__":

    print(
        "Starting process. If some images doesn't get picked up on the first time around, just rerun the script."
    )

    if not os.path.exists("games_cache.csv"):
        with open("games_cache.csv", mode="w") as games_cache_file:
            games_cache = csv.writer(
                games_cache_file,
                delimiter=",",
                quotechar='"',
                quoting=csv.QUOTE_MINIMAL,
            )

            games_cache.writerow(["id", "name", "filename"])

    for dirfile in os.listdir(r"."):
        img = existing_img(dirfile)
        if img:
            Game(img)

    args = sys.argv[1:]
    observer = Observer()
    observer.schedule(ImageHandler(), path=args[0] if args else ".")
    observer.start()

    print("Process started, listening for new files in this directory")

    try:
        while True:
            time.sleep(1)
    except Exception:
        observer.stop()

    observer.join()
