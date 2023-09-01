from os.path import isfile, join
import os

if __name__ == "__main__":
    data_files = []

    files = os.listdir("Programming-Assignment-Data")

    for file in files:
        if ".xml" in file:
            data_files.append(file)
