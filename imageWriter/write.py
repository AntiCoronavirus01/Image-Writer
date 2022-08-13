from asyncore import read
import string
import tkinter as tk
from tkinter import filedialog
from PIL import Image

root = tk.Tk()
root.withdraw()

print("Write Your Message (if u need file convert write \"file\")")
messageText = input(">>")
if messageText == "file":
    path = filedialog.askopenfilename()  
    f = open(path, "r")
    messageText = f.read()

#old alphabet var:
#["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"," "]
Alphabet = string.printable

# Set a size and mode, and create a new image.
width, height = (len(messageText), 1)
mode = 'RGB'
my_image = Image.new(mode, (width, height))


my_pixels = my_image.load()
s = 0
print("Started")
for char in messageText:  
    charUpper = char
    i = 0
    for letter in Alphabet:
        i += 1
        if  charUpper == letter:                        
            break;
    pixelColor = int((255 / len(Alphabet)) * i)
    print("Char Writed Pixel Code = " , pixelColor)    
    pixel = (pixelColor,pixelColor,pixelColor)  
    my_pixels[s,0] = pixel
    s +=1

my_image.save("text.png")
