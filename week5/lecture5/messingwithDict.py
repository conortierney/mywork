# messing with dictionaries

car = {                              # creates a dictionary object
   "make" : "ford",           # these are keys
   "model": "mondeo",
   "year" : 2010,
   "owner": {
        "name": "conor", 
        "driver-number": 2345
     }
}

print(car["year"])
print (car["owner"]["name"])
print (type (car["owner"].get("name")))
            

