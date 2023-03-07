
import random
user = input("Enter 'r' for rock, 'p' for paper or 's' for siscors")

computer = random.choice(['r', 'p', 's'])

# Rock is better than scissors
# Paper is better than Rock
# Scissors is better that paper

if user == 'r' and computer == 's':
    print("Computer selected scissors and you won")
if user == 's' and computer == 'r':
    print("Computer selected rock and you won")
if user == 's' and computer == 'p':
    print("Computer selected paper and you won")
if user == 's' and computer == 'r':
    print("Computer selected rock and you won")