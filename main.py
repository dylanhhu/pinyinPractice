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
import os
import time
import random

CHUNK = 1024

for root, dirs, files in os.walk("."):
    for filename in files:
        #if filename == "main.py":
         #   files.remove("main.py")
        #elif filename == ".DS_Store":
        #    files.remove(".DS_Store")
        if filename.find("wav") == -1:
            files.remove(filename)

print('files in folder:')
for filename in files:
    print(filename)

print("number of files:")
print(len(files))

input("ready?")

filesPlayed = []

for x in range(16):
    if x == 0:
        continue

    fileNo = random.randrange(0, len(files))
    filesPlayed.append(files[fileNo])
    
    for y in range(3):
        wave_obj = simpAud.WaveObject.from_wave_file(files[fileNo])
        play_obj = wave_obj.play()
        play_obj.wait_done()
        time.sleep(0.75)

for file in filesPlayed:
    print(file)
