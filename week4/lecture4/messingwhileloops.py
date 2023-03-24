# lecture wk4 | messing with while loops.
# program to count from 0-9 value.
# 1 = counter controlled loop
# 2  =  sentinal controlled loop.

count  = 0
while count < 12:
 print("count is", count) #instead of format function ("xxx", yyy)  1st varable as string and second as int inside brackets.
 count = count + 1                    # NB -  here make sure to change the condition.

print ("at the end count is", count)

count =10
while count >= 0:                     # always us : to finish 
 print ("countdown", count)
 count -= 1

print("blast off")               # do this print outside while loop.


#2 next: this is a sential controlled loop - that is until an event happens then program ends.
val = input("type something (q to quit):")
while val != "q":
 print ("not correct")
 val = input("no i said q to quit:")

print ("correct - finished loop")  #lopp stops when whats asked by used "q" is entered, otherwise "not correct" outputs.

