# Created by Alexander Li, 14/8/2020
# To print a series of text files to the terminal, creating a happy birthday message for Incy

import os # used for system calls, namely clear screen
import time # used for timing - controlling the framerate


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
        # add the contents of the file to frames. The content of each file will be a list of utf8 codes in a line.
        # ASCII would be fine too. But at this stage i'm thinking about using pre-made text files with special
        # characters. Which may use utf8 instead of plain ASCII.
        frames.append(f.readlines())
# SCREW THAT, I AM GOING TO TYPE OUT MY OWN ASCII. I AM GOING TO CREATE EVERYTHING BY MY OWN HANDS AND NO ONE CAN
# STOP MEEEEEEEEEEEEEEEEEEEE
# future Alex edit: trying to draw you in ascii did NOT work, holy shit


# start animation, repeat 42 times.
while True:
    # for each frame...
    for frame in frames:
        print("".join(frame)) # join everything into one string
        time.sleep(0.2) # sleep for 0.2 second
        os.system('cls') # clear screen

