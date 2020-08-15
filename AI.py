# Created by Alexander Li, 14/8/2020
# To print a series of text files to the terminal, creating a happy birthday message for ****

import os
import time


os.system('cls')
frame_count = 33 # set number of frames
file_names = [] # list of files we will use to create the animation
frames = [] # this will contain a list, each element being a frame. Each frame is a list of lines


# add all filenames
for i in range(frame_count):
    file_names.append("AI" + str(i + 1) + ".txt")


# for each filename
for name in file_names:
    # open the files. Don't ask why i use "with". No one understands why.
    with open(name, "r", encoding="utf8") as f:
        frames.append(f.readlines())


# start animation, repeat 42 times.
while True:
    # for each frame...
    for frame in frames:
        print("".join(frame)) # join everything into one string
        time.sleep(0.1) # sleep for 0.1 second for a 10fps animation
        os.system('cls') # clear screen

