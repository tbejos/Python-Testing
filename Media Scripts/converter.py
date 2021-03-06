# Author: Txanton Bejos
# Copies video and re-encode the audio to AAC with bitrate of 384 kb
import os
import subprocess

for file in os.listdir(os.getcwd()):
    if file[-3:] == "mkv" and file[-7:] != "new.mkv":
        # print file name minus extension
        print(file[:file.rfind(".")])
        # "command name", "-input", source file, "-codec:video", "copy from source",
        #"-codec:audio", "AAC", "-bitrate:audio", "384 kbps", output file (same name as input + " - new")
        command = ["ffmpeg", "-i", file, "-c:v", "copy", "-c:a", "aac", "-b:a", "384k", file[:-4]+" - new.mkv"]
        subprocess.call(command)
