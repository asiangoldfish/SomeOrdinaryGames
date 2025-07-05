import time
import hashlib


class SaveGameData:
    def __init__(self, name: str):
        self.id: str = self.generate_id()
        self.name: str = name

    def generate_id(self) -> str:
        res = hashlib.md5(str(time.time).encode())
        return res.hexdigest()


class SaveGameManager:
    def __init__(self):
        self.save_games = []

    def write_to_disk(self, save_name):
        """Save a game to disk.

        If the save game already exists, then overwrite it.

        Args:
            save_name (str): unique name for the save game. Will be displayed
                             to the player.
        """
        pass

    def load_from_disk(self, save_name):
        """Load a game from disk.

        Args:
            save_name (str): name of the save game to load.
        """
        pass

    def view_all_saves(self):
        """View all saved games on disk.
        """
        pass
