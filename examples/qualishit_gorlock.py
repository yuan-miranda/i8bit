#  examples/qualishit_gorlock.py
import sys
sys.path.append("../")

from PIL import Image
from main import quantize_image

NAME = "../media/gorlock.png"

def main():
    img = Image.open(NAME)
    width, height = img.size

    quantize_image(img.load(), width, height, 4)
    img.save("../output/img/qualishit_" + NAME.split(".")[0] + ".png")

if __name__ == "__main__":
    main()