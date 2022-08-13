import string
import tkinter as tk
from tkinter import filedialog
from PIL import Image

root = tk.Tk()
root.withdraw()

#old alphabet var:
#["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"," "]
Alphabet = string.printable
print("""Write start or file
      (if you write \"file\" image select custom filepath)""")

if input(">>") == "file":
    path = filedialog.askopenfilename()  
    my_image = Image.open(path)

    #my_image = open(path, "r")
else:
    my_image = Image.open("text.png")
    
print("Reading")
# open image and get size
width, height = (0, 0)

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
        text = text + Alphabet[index - 1]  
print("readed text is:")     
print(text)

