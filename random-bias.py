import random

maxrand = 9007199254740991
EVEN = 0
ODD = 0
tries = 0

while True:
   if ((random.randint(1, maxrand)) % 2) == 0:
      EVEN = EVEN + 1
   else: 
      ODD = ODD + 1
   tries = tries + 1

   print("Odd:", ODD, "Even:", EVEN, "Odd %:", ((ODD / tries) * 100), "Even %:", ((EVEN / tries) * 100), end='\r')
