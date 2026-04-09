from PlayerData.Player import Player, Gender
import Menu
from Text.animations import typewriter, elipses
from time import sleep


def intro():
    with open("src/enna/enna.txt", "r") as file:
        typewriter(file.read(), time_delay_seconds=0.001)
    typewriter("Welcome to ENNA")

    typewriter("What is your name?")
    name_prompt = Menu.StringInput(question="", check_if_correct=True)

    typewriter("Are you a male, or a female?")
    male_or_female = Menu.Menu("", "Male", "Female", check_if_correct=True)
    match male_or_female.CHOICE:
        case 1:
            gender = Gender.MALE
        case 2:
            gender = Gender.FEMALE
        case _:
            gender = Gender.OTHER
    player = Player(name_prompt.INPUT, gender)

    print("\n\nWelcome", player.player_name, "\n\n\n")
    sleep(1)
    typewriter("Except", create_newline=False)
    elipses(time_delay_seconds=1, create_newline=True)

    with open("src/enna/opening.txt", "r") as file:
        typewriter(file.read())

    typewriter("you", time_delay_seconds=1)
    player.save_player_data()
