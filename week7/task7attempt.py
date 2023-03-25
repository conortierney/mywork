# sample task 7 attempt
#ref: https://github.com/andrewbeattycourseware/pands-course-material/blob/main/jupyternotebooks/topic07-files.ipynb
# Files should be opened with the with open( filename, mode) as f: command
# real python

import sys                                       # import sys module to access command line arguments

if len(sys.argv) != 2:
    print("Usage: python count_e.py filename")
    sys.exit(1)

filename = sys.argv[1]                                # get filname from command line arguments using sys.argv

try:
    with open(filename, 'r') as file:                             # open the file
        count = 0                                                 # Initialize a counter variable to 0
        for line in file:                                         #for loop
            count += line.count('e') + line.count('E')            # Count both 'e' and 'E'
        print(f"The file {filename} contains {count} e's.")       # check for 
except FileNotFoundError:
    print(f"The file {filename} could not be found.")