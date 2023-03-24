
# ref/ ranges see lecture wk 5 
# w3 schools

import random

# Generate 10 random numbers between 0 and 100
numbers = [random.randint(0, 100) for i in range(10)]

# Print out the 10 random numbers
print("10 Random Numbers:")
print(numbers)

# Print out the top three numbers
print("Top Three Numbers:")
top_three = sorted(numbers, reverse=True)[:3]
print(top_three)
#oa