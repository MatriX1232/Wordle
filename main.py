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


def double_letters(word):
    for i in range (len(word)-1):
        if word[i] == word[i+1]:
            return True
    return False


def get_random_word() -> str:
    import random

    words = []
    with open("words.txt", "r") as file:
        words = file.read().splitlines()
    word = random.choice(words)
    while double_letters(word):     # a little bit of cheating
        word = random.choice(words)
    return word


if __name__ == "__main__":
    WORD = get_random_word().upper()
    print_cage(WORD, [Color.grey] * len(WORD))

    i = 0
    correct = False
    while not correct and i < 6:
        user_input = ""
        while len(user_input) != len(WORD):
            user_input = input("Enter word:").upper()
        colors = []
        correct = True
        for i, char in enumerate(user_input):
            if char == WORD[i]:
                colors.append(Color.green)
            elif char in WORD:
                colors.append(Color.yellow)
                correct = False
            else:
                colors.append(Color.red)
                correct = False
        print_cage(user_input, colors)
        i += 1

