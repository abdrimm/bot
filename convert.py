import os 
from numpy.lib.utils import source
import subprocess

if __name__ == "__main__":
    source = "dataset/ogg/"
    files = os.listdir(source)
    number_of_files = len(files)
    for i in range(number_of_files):
        current_file = files[i]
        destination = "dataset/wav/" + current_file[:-4] + ".wav" 
        print(source + current_file) 
        print(destination)                       
        subprocess.call(["ffmpeg", "-y", "-i", source + current_file, destination])
