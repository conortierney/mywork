# messing with functions
# demonstrating the defining and using functions

#x,y,z = (1,2,3)
#print (x,y,z, sep="", end="")            # sep and end are built in print functions
#print (f"{x} {y} {z}")             # f = formated string to print

def cube(number):
    print(number)
    return (number ** 3)


ans  = cube (23)
print (f"we got {ans}")

num = 45
print(f"and {num} is {cube(num)}")
