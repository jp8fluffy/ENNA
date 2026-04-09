from enum import StrEnum
from Text.animations import typewriter


class Menu:
    def __init__(
        self, menu_title: str, *menu_items, check_if_correct: bool = False
    ) -> None:

        menu = []
        for item in menu_items:
            menu.append(item)
        menu_length = len(menu)

        def prompt() -> int:
            print(menu_title)
            for index, menu_item in enumerate(menu):
                print(index + 1, " ", menu_item)
            user_input = input(f"Pick option [1-{menu_length}]: ")

            try:
                user_choice = int(user_input)
            except ValueError:
                print("Invalid input, please try again")
                prompt()
            else:
                selected_menu_item = menu[user_choice - 1]
                if user_choice > 0 and user_choice <= menu_length:
                    if check_if_correct:
                        yes_or_no = YesNoMenu(
                            f"You entered {selected_menu_item}, is this correct?"
                        )
                        if yes_or_no.CHOICE is UserInput.NO:
                            prompt()
                    return user_choice
                else:
                    print("Invalid input, please try again")
                    prompt()

        self.CHOICE = prompt()


class StringInput:
    def __init__(self, question: str, check_if_correct: bool = False) -> None:
        def prompt():
            print(question)
            user_input = str(input("Answer: "))
            if check_if_correct:
                yes_or_no = YesNoMenu(f"You entered {user_input} is this correct?")
                match yes_or_no.CHOICE:
                    case UserInput.YES:
                        return user_input
                    case UserInput.NO:
                        prompt()
                    case _:
                        raise RuntimeError(
                            "Something whent wrong asking user for value"
                        )

        self.INPUT = prompt()


class UserInput(StrEnum):
    YES = "yes"
    NO = "no"


class YesNoMenu:
    def __init__(self, question: str, default_answer: UserInput = UserInput.NO) -> None:
        self.QUESTION = question
        self.DEFAULT_ANSWER = default_answer
        self.CHOICE = self.prompt()

    def prompt(self):
        # Set the question to default so that when user presses enter it choices the capitalized letter
        match self.DEFAULT_ANSWER:
            case UserInput.NO:
                yes_no_string = "[y/ N]: "
            case UserInput.YES:
                yes_no_string = "[Y/n]: "

        typewriter(self.QUESTION)
        user_input = str(input(yes_no_string))
        match str.lower(user_input):
            case "y" | "yes" | "1" | "ye":
                return UserInput.YES
            case "n" | "no" | "0":
                return UserInput.NO
            case "":
                return self.DEFAULT_ANSWER

            case _:
                print("Not a valid answer")
                self.prompt()
