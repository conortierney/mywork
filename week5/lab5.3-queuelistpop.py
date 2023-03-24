#Create a program that puts 10 random numbers into a queue(list), the
#program should then output all the values in the queue, then take the
#numbers from the queue one at a time, print it and the current numbers still
#in the queue. (the command pop(0) takes the first element out of a list)


import random
queue  = []    #list
numberofnumbers  = 10
rangeto = 100

for n in range(0,numberofnumbers):
    queue.append(random.randint(0,rangeto))

print(f"queue is{queue}")

while len(queue) !=0:
    currentnumber = queue.pop(0)
    print (f"current number is {currentnumber} and the queue is {queue}")

print ("the queue is now empty")