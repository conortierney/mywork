# week 7
# messing with files lecture

FILENAME = "data.txt"

with open(FILENAME, 'rt') as f:   #open file name & path,   # if file doesnt exist= error, # use ls to check
    for data in f:             # reads in data one line at a time
      #print(data, end="")        # option
      print(data.strip())   # this correct line problems in output  , option 2



with open("data2.txt", "w+") as f:      # write mode
    f.write("how now\n")            #\n =new line
    f.write("brown cow\n")
    f.seek(0)                       # go to beginning of the file
    data = f.read()
    print(data)
print ("done")

