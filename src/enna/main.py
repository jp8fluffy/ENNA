import json
from pathlib import Path

PLAYER_SAVES_PATH = Path("playersaves.txt")

if __name__ == "__main__":
    if PLAYER_SAVES_PATH.exists():
        with open("playersaves.txt", "r") as save_files_directory:
            save_files_directory_data = save_files_directory.read()
    else:
        with open("playersaves.txt", "a+") as file:
            file.write("")
