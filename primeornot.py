c = 0
num = int(input("Enter any number : ")) 
if num > 1 :
    for i in range(2, int(num / 2)):
         if (num % i == 0):
              c = 1 
              break
    if c == 1:
         print("It is not a prime number")
    else:
         print("It is a prime number")
else:
    print("Enter another number")
