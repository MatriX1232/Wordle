class Color:
    # Reset color
    end = "\033[0m"

    # Preset colors
    red = "\033[31m"
    green = "\033[32m"
    blue = "\033[34m"
    cyan = "\033[36m"
    yellow = "\033[33m"
    magenta = "\033[35m"
    white = "\033[37m"
    black = "\033[30m"
    grey = "\033[90m"
    light_red = "\033[91m"

    # Bold preset colors
    bold_red = "\033[1;31m"
    bold_green = "\033[1;32m"
    bold_blue = "\033[1;34m"
    bold_cyan = "\033[1;36m"
    bold_yellow = "\033[1;33m"
    bold_magenta = "\033[1;35m"
    bold_white = "\033[1;37m"
    bold_black = "\033[1;30m"
    bold_grey = "\033[1;90m"
    bold_light_red = "\033[1;91m"

    @staticmethod
    def rgb(r: int, g: int, b: int, bold: bool = False):
        return f"\033[1;38;2;{r};{g};{b}m" if bold else f"\033[38;2;{r};{g};{b}m"

# class Color:
#     @staticmethod
#     def red(text: str = "This is red", bold: bool = False):
#         return f"\033[1;31m{text}\033[0m" if bold else f"\033[31m{text}\033[0m"

#     @staticmethod
#     def green(text: str = "This is green", bold: bool = False):
#         return f"\033[1;32m{text}\033[0m" if bold else f"\033[32m{text}\033[0m"

#     @staticmethod
#     def blue(text: str = "This is blue", bold: bool = False):
#         return f"\033[1;34m{text}\033[0m" if bold else f"\033[34m{text}\033[0m"

#     @staticmethod
#     def cyan(text: str = "This is cyan", bold: bool = False):
#         return f"\033[1;36m{text}\033[0m" if bold else f"\033[36m{text}\033[0m"

#     @staticmethod
#     def yellow(text: str = "This is yellow", bold: bool = False):
#         return f"\033[1;33m{text}\033[0m" if bold else f"\033[33m{text}\033[0m"

#     @staticmethod
#     def magenta(text: str = "This is magenta", bold: bool = False):
#         return f"\033[1;35m{text}\033[0m" if bold else f"\033[35m{text}\033[0m"

#     @staticmethod
#     def white(text: str = "This is white", bold: bool = False):
#         return f"\033[1;37m{text}\033[0m" if bold else f"\033[37m{text}\033[0m"

#     @staticmethod
#     def black(text: str = "This is black", bold: bool = False):
#         return f"\033[1;30m{text}\033[0m" if bold else f"\033[30m{text}\033[0m"

#     @staticmethod
#     def rgb(r: int, g: int, b: int, text: str = "This is custom color", bold: bool = False):
#         return f"\033[1;38;2;{r};{g};{b}m{text}\033[0m" if bold else f"\033[38;2;{r};{g};{b}m{text}\033[0m"