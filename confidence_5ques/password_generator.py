import random

letter = "abcdefghijklmnopqrstuvwxyz"
number = "0123456789"
symbols="!@#$%^&*"

length = int(input("enter password length:"))

password = ""
all_char = letter+ number+ symbols

for i in range(length):
    password+= random.choice(all_char)

print("generated password is: ", password)
