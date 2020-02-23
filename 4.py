

# Μετατρέπω το s σε ASCII και κρατάω το ελέγχω μόνο το τελευταίο στοιχείο της λίστας 
s = 'bhjk'
k = [ord(c) for c in s]
print (k)
last = (k[-1])


if k > 1:
  
   for i in range(2,last):
       if (last % i) == 0:
           print(k,"is not a prime number")
           print(i,"times",last//i,"is",last)
           break
   else:
       print(k,"is a prime number")
       

else:
   print(k,"is not a prime number")

