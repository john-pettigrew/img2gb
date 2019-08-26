#! /usr/bin/python3

import sys
from PIL import Image

hex_map = {
        56:("1", "1"),
        98:("1", "0"),
        172:("0", "1"),
        188:("0", "0"),
}



if len(sys.argv) != 2:
    print("Usage is: image2gb [image_path]")
    exit(1)

values = []


image_path = sys.argv[1]

im = Image.open(image_path)
width, height = im.size

for x in range(0, width, 8):
    for y in range(0, height):
        byteA = ""
        byteB = ""

        for current_pixel in range(0, 8):
            colors = im.getpixel((x + current_pixel, y))
            byteA += hex_map[colors[1]][1]
            byteB += hex_map[colors[1]][0]


        values.append('0x' + format(int(byteA, 2), '02x'))
        values.append('0x' + format(int(byteB, 2), '02x'))


print("unsigned char MySprite[] =\n{\n", end='')
for i in range(0, len(values), 8):
    print('\t', end='')
    for j in range(0, 8):
        print(values[i + j] + ', ', end='')
    print('\n', end='')
print("};\n", end='')
