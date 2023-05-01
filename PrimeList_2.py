import PrimeNumber
from PrimeNumber import *
end = int(input("Enter a number:  "))
numList = range(1, end)

for num in numList:
    if isPrimeFunction(num):
        print(num)