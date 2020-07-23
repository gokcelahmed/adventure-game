# imports
import time
import random
import os


# clear terminal
def clear():
    os.system("cls")


# Menu Selection
def menu_selection():
    clear()
    valid = True
    while valid:
        print("Welcome to the adventure game!")
        print("Please pick one of the following options:")
        print("a -> start")
        print("b -> exit")
        option = input("Please make a choice(a/b): ").lower()
        if option == "a":
            print("You have selected to play the game")
            valid = False
            start_game()
        elif option == "b":
            print("Good Bye!")
            valid = False
            exit()
        else:
            print("Please make a valid choice")
            clear()


# start_game
def start_game():
    clear()
    valid = True
    while valid:
        print("You are walking through the woods in complete darkness")
        print("There are two paths towards you, one to the left and one to the right")
        print("Please pick one of them...")
        option = input("Please make a choice(right/left): ").lower()
        if option == "right":
            print("You picked the path to the right")
            valid = False
            right_path()
        elif option == "left":
            print("You picked the path to the left")
            valid = False
            left_path()
        else:
            print("Please make a valid choice")
            clear()


# Path to the right
def right_path():
    clear()
    valid = True
    while valid:
        print("You fall into a ditch and die...")
        print("Game Over!!!!")
        valid = False
        menu_selection()


# Path to the left
def left_path():
    clear()
    valid = True
    while valid:
        print("You encounter and Ogre")
        print("You have two choices: either to fight him or run")
        option = input("Please make a choice(fight/run): ").lower()
        if option == "fight":
            continue
        elif option == "run":
            continue
        else:
            print("Please make a valid choice")
            clear()

menu_selection()