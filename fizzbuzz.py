import sys

if len(sys.argv)>=2:
  try:
    int(sys.argv[1])
  except ValueError:
    print "Fizzbuzz only accepts integers!"
    sys.exit(0)
  limit = int(sys.argv[1])
else:
  try:
    limit = int(raw_input("What do you want to count up to?"))
  except ValueError:
    limit = int(raw_input("Fizzbuzz only accepts integers! Enter one:"))
     
print "Fizzbuzz counting up to {}".format(limit)

for n in range (1, limit+1):
   if n % 15 == 0:
      print "fizzbuzz"
   elif n % 5 == 0:
      print "buzz"
   elif n % 3 == 0:
      print "fizz"
   else:
      print n
