# ==================
#  Pinyin Dictation
#     Practice
#
#      V 1.0
#
#    By Dylan Hu
#
# ==================

# ==================
#       TODO
# 1: Makesure that
#    sounds aren't
#    repeated more
#    than once.
# ==================


import simpleaudio as simpAud
import sys, os, time, random
import test, func, learn

columns, rows = os.get_terminal_size(0)  # Get the screen size to be able to clear it.

func.clear(rows)  # Clear the screen

print("Welcome to Dylan's Pinyin Learning Tool")
print("Made with love by Dylan")

time.sleep(1)  # Sleep for 1 second so that user can read the text

func.clear(rows)

while True:
    print("What do you want to do?")
    print("Learn or Test")
    print("L/T\n")

    userInput = input(">>>")

    if userInput == "L":
        func.clear(rows)
        learn.function()
        func.clear(rows)
    elif userInput == "T":
        func.clear(rows)
        test.function()
        func.clear(rows)
    else:
        print("You typed an invalid character: " + str(userInput) + '\n')
