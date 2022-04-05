# autoclick button on website

# import modules
import time
from tkinter.tix import Y_REGION
import pyautogui


links = []

def load_list():
    """
    load txt file
    """
    # open file
    with open('list.txt', 'r') as f:
        # read file
        lines = f.readlines()
    for line in lines:
        links.append(lines)

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
    for link in links:
        print(link)
        click((146, 657))
        write(link)
        time.sleep(5)
        click((846, 176))
        time.sleep(5)