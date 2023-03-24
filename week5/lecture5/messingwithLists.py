# messing w lists
# wk 5 lecture
# concatinate lists ADD, print len of a list
# he main distinguishing feature of tuples is that they are immutable:cannot be modified.
# this means that once they are created, their size and contents cannot be changed:


#1
boats = ['sigma', 23, 'speed']         # define list elements int and 'str'
boats = boats + [1,2,3]               # Addition concatenates lists
print (boats)                   
#2
list = ['a', 'b', 3]
print (len (list))                  # Length of a list

#3 for loop in lists// type of boats 
boats = ['sigma', 23, 'speed']         
for boat in boats:
    print(type(boat))        # outputs types: str, int,str  .    

#4 
ages = [12,14,16,]    #note all int
sum = 0
for age in ages:
    sum += age
print (sum)

#5 - eaxmple bankacc
string = "1234567890"
print (string[-6:])
