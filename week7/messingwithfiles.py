# week 7
# messing with files lecture

FILENAME = "data.txt"

with open(FILENAME, 'r') as f:   #open file name & path,   # if file doesnt exist= error, # use ls to check
    for data in f:             # reads in data one line at a time
      #print(data, end="")        # option
      print(data.strip())   # this correct line problems in output  , option 2

