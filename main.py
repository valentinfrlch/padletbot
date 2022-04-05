import time
from tkinter.tix import Y_REGION
import pyautogui
from get_content import *

links = []

def load_list():
    """
    load txt file
    """
    # open file
    with open('websites.txt', 'r') as f:
        # read file
        lines = f.readlines()
    for line in lines:
        try:
            line = line.split("[")[1].split("]")[0].split("\n")[0]
            links.append(line)
        except IndexError:
            pass

def click(coordinates):
    # click button
    pyautogui.click(x=coordinates[0], y=coordinates[1])
    # wait for 1 second
    time.sleep(1)

def write(text):
    # write text
    pyautogui.typewrite(text)
    # wait for 1 second
    time.sleep(1)   

def mainloop():
    print("GO in t-3 seconds")
    time.sleep(1)
    print("GO in t-2 seconds")
    time.sleep(1)
    print("GO in t-1 seconds")
    time.sleep(1)
    print("Here we GO!")
    #load_list()
    links = get_links("amogus sus gif")
    for link in links:
        print(link)
        click((427, 657)) #146, 657 for first tab
        time.sleep(0.3)
        click((872, 387))
        write(link)
        click((964, 194))
        time.sleep(1)
        click((1100, 234)) #846, 176 for publish on first tab
        time.sleep(1)

mainloop()