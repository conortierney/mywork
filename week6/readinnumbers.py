# read in 2 numbers and numtiply them
# practice for refactor code - that is code you can use again 
# not essential material

# using default and messages
def readNum(message = "enter a number:"):
    num = False
    while (not num):            # another way/while (num == False):
        try:
            num = int(input(message))
        except ValueError:
         print("thats not a number,: ", end="")
    return num                      # can put all of the above in a seperate file

num1 = readNum()
num2 = readNum("enter num2:")

answer = num1 * num2

print(f"answer is {answer}")

