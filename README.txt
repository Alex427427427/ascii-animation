PRELIM: 
windows: 
  download vlc media player (64 bit!)
  pip install python-vlc
  pip install pillow

RUN:
Clone repo. Double click AI.py to run.
Maximise the screen at the command terminal during runtime for proper display. 
If double clicking on AI.py doesn't work, make sure you have python downloaded, 
then open your command prompt, cd to the local repo directory, then enter the command "python.exe AI.py"

IF ON LINUX: in AI.py, edit every occurrence of os.system('cls') into os.system('clear').
Adjust the number in time.sleep(number) as you see fit.
(Linux also appears to result in a speed that's more faithful to the number we set. 
On Windows, having time.sleep(0.02) should have given 50fps, completing the 33 frames in 0.66 seconds, but that was not the case.
It actually results in a much slower rate that was originally desired. That's why it is set to 0.02.
You may edit that number depending on your OS.)

If curious, may check out the png2ascii.py file, in which i convert the pixel values of png files into ascii. 


HOW TO PUT IN YOUR OWN ANIMATION:

1. Delete all "AI[number].png" and "AI[number].txt" files.

2. Draw up the frames in any image editing software and save as PNG. Keep in mind the final printed result will look twice as high. 
For example, the terminal when maximised can display about 70 lines of 240 characters each. If you want to use up the entire space, 
you would draw your frames with 240 horizontal pixels and 70 vertical pixels. While drawing, you are imagining what it would look like 
when elongated in the vertical direction. I have used 128 horizontal pixels and 64 vertical pixels in my frames.
Save all the images in the same directory as png2ascii.py
For convenience later, name all of them in the format "AI[frame number].png". Frame number starts at 1.

3. Inside png2ascii.py:
edit the framecount variable to how many frames you have. Then run the file. You will end up with all the .png files converted to .txt files. 
The original .png files will still be there.

4. Inside AI.py:
edit the framecount variable to how many frames you have. 

5. From now on, when you double AI.py to run, the terminal will display your animation.
