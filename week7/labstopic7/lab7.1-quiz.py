# topic 7 lab, files
# 
# the with statement will automatically close the file
# when it is finished with it

# A

with open("test-a.txt") as f:
 data = f.read()
 print (data)

# . The program will throw an error, the default mode is ‘r’ ie read, and read
#will throw an error if the file does not exist.


#B AND C
with open("test-b.txt", "w") as f:
 data = f.write("test b\n")                # returns the number of chars written = 7
 print (data)


with open("test-b.txt", "w") as f2:              # open file again
 data = f2.write("another line\n")        #13 characters
 print (data)


#D write mode w
with open("test-d.txt", "w") as f:
 data = f.write("test d\n")               # returns the number of chars written
 print (data)

with open("test-d.txt", "a") as f2:         # open file again
 data = f2.write("another line\n")
 print (data)



