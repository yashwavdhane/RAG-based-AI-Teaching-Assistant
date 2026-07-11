import os
import subprocess
files = os.listdir("videos")
for file in files:
    f_no = file.split("]")[1].split(",")[0]
    f_name = file.split(",")[1].split(".")[0]
    subprocess.run(["ffmpeg","-i",f"videos/{file}",f"audios/{f_no}{f_name}.mp3"])