from PIL import Image

ASCII_CHARS = " .:-=+*#%@"
name = "gorlock.png"
color_depth = len(ASCII_CHARS)

def quantize_color(color, n=8):
    return int(color / 256 * n) * int(256 / n)

def quantize_pixel(r, g, b, n=8):
    # uncomment the line below to use the luminance formula (grayscale)
    # r = g = b = int(0.299 * r + 0.587 * g + 0.114 * b)
    return (quantize_color(r, n), quantize_color(g, n), quantize_color(b, n))

def quantize_image(pixels, width, height, n=8):
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y][:3]
            pixels[x, y] = quantize_pixel(r, g, b, n)

def to_ascii(pixels, width, height, ascii_chars):
    line = ""
    for y in range(height):
        for x in range(width):
            gray = pixels[x, y][0]
            line += ascii_chars[gray * color_depth // 256]
        line += "\n"
    return line

def resize_image(image, new_width=100):
    width, height = image.size
    ratio = (height // 2.6) / width
    # ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def main():
    img = Image.open(name)
    pixels = img.load()
    width, height = img.size

    quantize_image(pixels, width, height, color_depth)
    img.save("quantized_" + name)

    # 1x1 size ascii art (original size)
    # ascii_art = to_ascii(pixels, width, height, ASCII_CHARS)
    # with open("ascii_" + name.split(".")[0] + ".txt", "w") as f:
    #     f.write(ascii_art)

    # resized ascii art
    img = resize_image(img)
    pixels = img.load()
    width, height = img.size
    ascii_art = to_ascii(pixels, width, height, ASCII_CHARS)
    with open("ascii_resized_" + name.split(".")[0] + ".txt", "w") as f:
        f.write(ascii_art)

if __name__ == "__main__":
    main()
