

import glob
import os
import time
dir_name = 'C:/Users/basmi/Guru99/'
#dir_name = 'C:/Program Files/Java/jdk1.8.0_191/'
# Get list of all files only in the given directory
list_of_files = filter( os.path.isfile,
                        glob.glob(dir_name + '*') )
# Sort list of files based on last modification time in ascending order
list_of_files = sorted( list_of_files,
                        key = os.path.getmtime)
# Iterate over sorted list of files and print file path
# along with last modification time of file
for file_path in list_of_files:
    timestamp_str = time.strftime(  '%m/%d/%Y :: %H:%M:%S',
                                time.gmtime(os.path.getmtime(file_path)))
    print(timestamp_str, ' -->', file_path)