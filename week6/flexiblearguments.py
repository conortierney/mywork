# more messing with functions
# flexible arguments

print (1,2,3, sep="",end="\t")              # variables here work in any order
print ("hi")

#unnamed args
def fun1(*args):
    print(type(args))        # type args = tuple
    print(args)
    for val in args:
        print(val)


#fun1("a", "b", "c")

# keyword arguments
def  fun2(**kwargs):
    print(type(kwargs))            # kwargs here was a dictionary
    print (kwargs)

    # for val in args
    #print(val)

#fun2(name="joe", age=21, gender="m")         # these are the arguments

# sample code average of numbers
def ave(*values):
    number_of_values = len(values)
    sum= 0
    for value in values:                
        sum+= value                         # there is also a sum function in python

    average = sum / number_of_values
    return average


av1, sum_of_numbers = ave(1, 2, 3, 4, 5, 6)    # error as not defined somewhere

print(f"{av1} and sum is {sum_of_numbers}")


