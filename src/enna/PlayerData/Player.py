from enum import StrEnum, Enum, IntEnum
from pathlib import Path
import json


class PlayerStatus(Enum):
    ALIVE = True
    DEAD = False


class Gender(StrEnum):
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"


class Chapter(IntEnum):
    INTRO = 0
    ONE = 1
    TWO = 2


class Player:
    health: int = 100
    nicotine: int = 100
    saves = 0

    def __init__(self, player_name: str = "Orion", gender: str = Gender.MALE) -> None:
        self.player_name = player_name
        self.gender = gender
        self.chapter = Chapter.INTRO

    def heal(self, regen_amount: int):
        self.health += regen_amount

    def die(self):

        print("you died")

    def take_damage(self, damage_amount: int):
        if damage_amount >= self.health:
            self.die()
        else:
            self.health -= damage_amount

    def save_player_data(self):
        player_data = {
            "playerName": self.player_name,
            "playerGender": self.gender,
            "playerStats": {
                "chapter": self.chapter,
                "health": self.health,
                "nicotine": self.nicotine,
            },
        }
        save_file_name = Path(f"{self.player_name}{self.saves}.json")
        with open(save_file_name, "x") as file:
            file.write(json.dumps(player_data, indent=4))
        self.saves += 1

        with open('playersaves.txt', 'a') as player_saves_file:
            player_saves_file.write(str(save_file_name))


    def check_for_player_save_data(self, save_number:int=0):
        save_file_name = Path(f"{self.player_name}{save_number}.json")
        try:
            with open(save_file_name, 'r') as player_data_file:
                stored_player_data = json.load(player_data_file)
        except FileNotFoundError:
            if self.saves > 0:

