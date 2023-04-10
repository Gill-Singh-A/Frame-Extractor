# Frame Extractor
Extracts each frame of the specified Video File

## Requirements
Language Used = Python3<br />
Modules/Packages used:
* cv2
* sys
* pathlib
* os
* time
* datetime
* colorama

## Input
It takes input through the command by which we run the python file.<br />
If we specify '*' then it will extract the frames of all the video files present in the folder. For example:
```bash
python frame_extractor.py *
```
Otherwise we have to specify the file names of the video files that are present in the folder in which the program is run. For example:
```bash
python frame_extractor.py video_file_1 video_file_2 ...
```

## Output
It will make a new folder with the name "Frames", in the folder "Frames" it will create new folders with name of each video file and extract the frames of respective video file in their respective folders.