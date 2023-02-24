# messing w strings - lecture3 
#Author : Andrew
# showing:
# escape characters 1
# adding numbers to strings( task 3 eg) 2
# splicing 3

#1
astring = "he said\"hello\" "
print (astring)

#2
mark = 33
string2 = "your mark is:"+str(mark)
print (string2)

#3 
accountno = "123456789"
print (accountno[0:4])

accountnumber = 1234567890
string = "please enter a 10 digit account number{}:"+str(accountnumber)
print (string.replace("123456", "xxxxxxx"))

