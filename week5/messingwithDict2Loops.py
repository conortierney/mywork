# messing with loops in dictionary

car = {
    "make":"fiat",                      # keys = make, model price and tags.
    "model":"punto",
    "price": 1000,
    "tags" : ["preowned","bestbuy","dealer"]
}
'''
for key in car:
    print (key, "has value", car [key])
    '''


for key, value in car.items():
    print (key, 'has value', value)
    