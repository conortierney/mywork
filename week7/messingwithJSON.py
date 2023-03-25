
# see lab for more


import json

electricBill = {
    'name' : 'Andrew',
    'amount' : '99999'
}

with open("storedata.json", "wt") as f:
    json.dump(electricBill, f)                      # writes the dictionary object to the file as a JSON object