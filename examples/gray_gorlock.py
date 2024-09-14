# examples/gray_gorlock.py
import sys
sys.path.append("../")

from PIL import Image
from main import grayscale_image

NAME = "../media/gorlock.png"

def main():
    img = Image.open(NAME)
    width, height = img.size

    grayscale_image(img.load(), width, height)
    img.save("../media/img/gray_" + NAME.split(".")[0] + ".png")

if __name__ == "__main__":
    main()