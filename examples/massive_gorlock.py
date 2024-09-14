# examples/massive_gorlock.py
import sys
sys.path.append("../")

from PIL import Image
from main import resize_image

NAME = "../media/gorlock.png"

def main():
    img = Image.open(NAME)
    width, height = img.size

    # LMAO
    img = resize_image(img, width * 100)
    img.save("../media/img/massive_" + NAME.split(".")[0] + ".png")

if __name__ == "__main__":
    main()