from Colors import Color

def print_cage(characters: str, colors: list) -> None:
    g = 100
    characters = list(characters)
    for c in characters:
        print(Color.rgb(g, g, g) + "|-----|" + Color.end, end="     ")
    print()

    for i, char in enumerate(characters):
        print(Color.rgb(g, g, g) + f"|  {colors[i] + char + Color.rgb(g, g, g)}  |" + Color.end, end="     ")
    print()

    for c in characters:
        print(Color.rgb(g, g, g) + "|-----|" + Color.end, end="     ")
    print()


def get_random_word() -> str:
    import random

    words = []
    with open("words.txt", "r") as file:
        words = file.read().splitlines()
    return random.choice(words)


if __name__ == "__main__":
    print_cage(get_random_word(), [Color.green, Color.red, Color.blue, Color.cyan, Color.yellow])
