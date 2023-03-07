username = input("Enter your name: ")
password = input("Enter your password: ")
numberOfCharacters = len(password)
while numberOfCharacters < 8:
    print("Password should be at least 8 characters long!")
    password = input("Enter your password: ")
    numberOfCharacters = len(password)

print(f"Hello {username} your password is {password}")