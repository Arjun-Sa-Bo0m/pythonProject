# program to tell user if the number is prime number

num = int(input("Enter any number:  "))
counter = 2
isPrime = True
while counter < num:
    if num % counter == 0:
        isPrime = False
        break
    else:
        counter = counter + 1
if isPrime:
    print("This number is a prime number!")
else:
    print("This number is not a prime number!")
