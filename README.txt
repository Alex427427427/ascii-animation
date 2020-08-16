Download; have everything in the same folder, then double click AI.py to run.
Maximise the screen at the command terminal during runtime for proper display. 
EDIT: Some people could not get things to work just by running AI.py, so I've added AI.exe that should just run it with no problems. 

IF ON LINUX: edit every occurrence of os.system('cls') into os.system('clear').
(Linux also appears to result in a speed that's more faithful to the number we set. 
On Windows, having time.sleep(0.02) should have given 50fps, completing the 33 frames in 0.66 seconds, but that was not the case.
So you may edit that number depending on your OS.)

If curious, may check out the png2ascii.py file, in which i convert the pixel values of png files into ascii. 
