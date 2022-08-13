from random import randint

from PIL import Image

Alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"," "]

print("Reading")
# open image and get size
width, height = (0, 0)
my_image = Image.open("text.png")
width = my_image.width
height = my_image.height

# Load all the pixels.
rgb_im = my_image.convert('RGB')
text = ""
# Loop through all the pixels, and read all and get chars
for y in range(height):
    for x in range(width):   
        r, g, b = rgb_im.getpixel((x, y))
        index = 0
        for i in range(len(Alphabet)):            
            if int((255 / len(Alphabet)) * i) == r:
                break;
            index += 1
        text = text + Alphabet[index - 1].lower()   
print("readed text is:")     
print(text)

