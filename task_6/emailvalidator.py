import re
from tkinter import *

def validateemail(email):
    return re.match(r'[\w-]{1,20}@\w{2,20}\.\w{2,3}$',email)

def emailvalidator():
    email=username.get()
    valid=validateemail(email)
    if valid:
        Label(screen, text="Email Id is Valid").pack()
    else:
        Label(screen, text="Email Id is Invalid").pack()

    Button(screen, text="Check New Email Address",width=20,height=1,command=main_screen).pack()


def main_screen():
    global screen
    screen=Tk()
    global username
    username=StringVar()
    screen.geometry("300x200")
    screen.title("Email Address Validator")
    Label(screen, text="Please Enter the Email address below").pack()
    Entry(screen,textvariable=username).pack()
    Button(screen, text="Validate",width=10,height=1,command=emailvalidator).pack()


main_screen()
