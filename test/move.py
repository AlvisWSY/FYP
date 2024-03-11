import os
import random
import shutil

# Source and destination directories
source_dir = "/media/mldadmin/home/s123mdg34_04/WangShengyuan/FYP/testdata/data/train/noise"
destination_dir = "/media/mldadmin/home/s123mdg34_04/WangShengyuan/FYP/testdata/data/test/noise"

# Get the list of files in the source directory
file_list = os.listdir(source_dir)

# Calculate the number of files to move (20% of the total files)
num_files_to_move = int(len(file_list) * 0.2)

# Randomly select the files to move
files_to_move = random.sample(file_list, num_files_to_move)

# Move the selected files to the destination directory
for file_name in files_to_move:
    source_path = os.path.join(source_dir, file_name)
    destination_path = os.path.join(destination_dir, file_name)
    shutil.move(source_path, destination_path)

print("Files moved successfully!")
