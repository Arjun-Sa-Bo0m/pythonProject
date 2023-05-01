# is prime function:
usernum = int(input("Enter any number"))
v = list(range(1,num))
for num in v:
    counter = 2
    isPrime = True
    while counter < num:
         if num % counter == 0:
            isPrime = False
            break
         else:
        counter = counter + 1
    if isPrime:
        print(num)


