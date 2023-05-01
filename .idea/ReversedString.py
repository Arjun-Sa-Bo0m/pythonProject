def reverseString(Str):
    counter = len(Str) - 1
    rev = ""
    while counter>= 0:
        rev = rev + Str[counter]
        counter = counter - 1

    return rev
name = input("What to know your name backwords? Type it here to know if it is a pelendrome: ")
print(reverseString(name))
if name == (reverseString(name)):
    print("Your word is a pelendrome!")
else:
    print("Not a pelendrome")
