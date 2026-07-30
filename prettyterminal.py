import platform
# Format Codes
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
ITALIC = '\033[3m'

# Color escape codes
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
PURPLE = '\033[;35m'
RESET = '\033[0m'  # Clear all styles

# Characters
BOX_DRAWING = ["═", "║", "╔", "╗", "╚", "╝", "╠", "╢", "╣", "╦", "╩", "╬"]
TODO = "☐"
CROSSED = "☒"
ARROW = "→"
HEARTS = f"{RED}♥{RESET}"
DIAMONDS = f"{RED}♢{RESET}"
SPADES = f"♠"
CLUBS = f"♧"
SMILEFACE = "😊"
SADFACE = "🙁"
TURTLE = f"{GREEN}🐢{RESET}"
# Windows for some reason has the UTF Checked box reversed. So we need to check which os we are using to use the right character.
os_type = platform.system()
if os_type == "Windows":
    TICKED = "🗹"
else:
    TICKED = "☑"

def trueLength(line):
    colours = (GREEN, PURPLE, BLUE, RED, YELLOW, MAGENTA, RESET)
    for colour in colours:
        if colour in line:
            line = line.replace(colour, "")
    if '🐢' in line:
        turtle = True
        return len(line) + 1

def printHeading(line, track=True):
    raw = line.strip()
    line_length = trueLength(raw)
    top_border = GREEN + "╔" + ("═" * (line_length + 2)) + "╗"
    heading = f"║ {RESET}{raw}{GREEN} ║"
    bot_border = "╚" + ("═" * (line_length + 2)) + "╝" + RESET
    print(top_border)
    print(heading)
    print(bot_border)
