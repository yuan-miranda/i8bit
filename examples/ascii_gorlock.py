# examples/example.py
import sys
sys.path.append("../")

from PIL import Image
from main import to_ascii

ASCII_CHARS = " .:-=+*#%@"
NAME = "../media/gorlock.png"

def main():
    img = Image.open(NAME)
    width, height = img.size

    ascii_art = to_ascii(img.load(), width, height, ASCII_CHARS)
    with open("../media/ascii/ascii_" + NAME.split(".")[0] + ".txt", "w") as f:
        f.write(ascii_art)

if __name__ == "__main__":
    main()
