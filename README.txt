Download; have everything in the same folder, then double click AI.py to run.
Maximise the screen at the command terminal during runtime for proper display. 
If double clicking on AI.py doesn't work, open your command prompt, cd to the directory, then enter the command "python.exe AI.py"

IF ON LINUX: edit every occurrence of os.system('cls') into os.system('clear').
(Linux also appears to result in a speed that's more faithful to the number we set. 
On Windows, having time.sleep(0.02) should have given 50fps, completing the 33 frames in 0.66 seconds, but that was not the case.
So you may edit that number depending on your OS.)

If curious, may check out the png2ascii.py file, in which i convert the pixel values of png files into ascii. 
