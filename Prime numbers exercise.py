#Check given number is prime number or not
i=int(input("Enter a number to find out whether the number is prime or not:"))
if (i == 2 or i == 3 or i == 5 or i ==7):
    print('Prime number')
elif (i%2==0) or (i%3==0) or (i%5==0) or (i%7==0):
    print('Not a prime number')
else:
    print('prime number')

