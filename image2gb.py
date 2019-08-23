#! /usr/bin/python3

import sys
from PIL import Image

def print_hex(value):
    print("0x{:02x}".format(value), end='')


if len(sys.argv) != 2:
    print("Usage is: image2gb [image_path]")
    exit(1)

print("unsigned char MySprite[] =\n{\n", end='')

image_path = sys.argv[1]

im = Image.open(image_path)
width, height = im.size

for y in range(0, height):
    for x in range(0, width):
        colors = im.getpixel((x, y))
        if colors[1] == 0:
            print_hex(colors[1])
        else:
            print_hex(colors[1] + 67)

        if x == width - 1:
            print()
            if y == height - 1:
                continue;
        else:
            print(", ", end='')


print("};\n", end='')
