from time import sleep


def typewriter(
    text: str, time_delay_seconds: float = 0.061, create_newline: bool = True
) -> None:
    for char in text:
        print(char, end="", flush=True)
        sleep(time_delay_seconds)
    if create_newline is True:
        newline()


def elipses(time_delay_seconds: float = 0.1, create_newline: bool = True):
    for i in range(3):
        print(".", end="", flush=True)
        sleep(time_delay_seconds)
    if create_newline is True:
        newline()


def newline():
    print("")
