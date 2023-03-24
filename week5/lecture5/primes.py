# generate prime no.s
# use for functions in week 6.

primes = []
upto = 101

for candidate in range (2, upto):                           # print (candidate)
   isprime = True
   for divisor in primes:
      if (candidate % divisor ==0):
         isprime = False
         break
      

      if isprime:
         primes.append(candidate)
   
print (primes)

