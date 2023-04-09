import os

#check all file and store a array

all_file = os.listdir()

#check isfile

for file in all_file:
    if os.path.isfile(file):
        if file== "auto create and move file.py":
            continue
        try:
            # Create target Directory
            os.mkdir(file[:-4])
        except FileExistsError:
            print("Directory " , file ,  " already exists")
