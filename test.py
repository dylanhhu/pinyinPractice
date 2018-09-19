import simpleaudio as simpAud
import os
import time
import random

def function():
    for root, dirs, files in os.walk("assets"):
        for filename in files:
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
            wave_obj = simpAud.WaveObject.from_wave_file("assets/" + files[fileNo])
            play_obj = wave_obj.play()
            play_obj.wait_done()
            time.sleep(0.75)

    for file in filesPlayed:
        print(file)
