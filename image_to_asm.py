from PIL import Image

image = Image.open("image.png")
image = image.convert("RGB")
width, height = image.size

file = open("output.txt", "w")

hex_per_line = 0
for y in range(height):
    for x in range(width):
        r, g, b = image.getpixel((x, y))

        r = hex(r)[2:]
        if len(r) == 1:
            r = "0" + r
        g = hex(g)[2:]
        if len(g) == 1:
            g = "0" + g
        b = hex(b)[2:]
        if len(b) == 1:
            b = "0" + b

        if hex_per_line % 512 == 0:
            file.write("\n\t")
        file.write("0x00" + r + g + b + ", ")
        hex_per_line += 1