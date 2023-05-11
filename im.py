#!/usr/bin/env python

from tkinter import Tk
from PIL import Image, ImageDraw, ImageFont
import os
import random
import textwrap
import time

i = 1
#set the image as wallpaper
def set_wallpaper(name):
    os.system("xfconf-query --channel xfce4-desktop --property /backdrop/screen0/monitorDP-3/workspace0/last-image --set {name}")


with open('.quran.txt') as f:
  for text in f:
    wait_time = len(text) * 0.2

    # create a tkinter window and hide it
    root = Tk()
    root.withdraw()

    # get the screen size
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # create a new image
    image = Image.new('RGB', (screen_width, screen_height), color='black')

    # define the font and maximum width of each line
    
    font = ImageFont.truetype('quran.otf', size=36)
    max_width = screen_width - 700  # adjust as needed

    # wrap the text into lines based on the maximum width
    lines = textwrap.wrap(text, width=max_width // font.getsize(' ')[0])

    # draw each line centered on the image
    draw = ImageDraw.Draw(image)
    y_text = (screen_height - len(lines) * font.getsize(lines[0])[1]) // 2
    for line in lines:
        text_width, text_height = draw.textsize(line, font)
        x_text = (screen_width - text_width) // 2
        draw.text((x_text, y_text), line, font=font, fill='white')
        y_text += font.getsize(line)[1]

    # save the image
    if i == 1:
        name = 'output.png'
    else:
        name = 'output1.png'
    image.save(name)
    if i == 1:
        os.system("xfconf-query --channel xfce4-desktop --property /backdrop/screen0/monitorDP-3/workspace0/last-image --set output.png")
        i = 0
    else:
        os.system("xfconf-query --channel xfce4-desktop --property /backdrop/screen0/monitorDP-3/workspace0/last-image --set output1.png")
        i = 1
    time.sleep(wait_time)



