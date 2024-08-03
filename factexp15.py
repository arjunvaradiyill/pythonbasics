num = int(input("Enter any number : "))
print (1, end=' ') #1 is a factor of every number
f = 2
while f <= num :
     if num % f == 0: 
          print(f, end=' ')
     f += 1
