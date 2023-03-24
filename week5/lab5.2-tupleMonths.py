#Create a tuple that stores the months of the year, from that tuple create
#another tuple with just the summer months (May, June, July), print out the
#summer months one at a time.
# tuple = ()


months =("January",
"February",
"March",
"April",
"May",
"June",
"July",
"August",
"September",
"October",
"November",
"December"
)

summer = months[4:7]           # may = 4 , july
for month in summer:           #for loop
   print (month)