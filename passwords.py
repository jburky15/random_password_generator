import random

#Set values to be randomized
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
symbols = "!@#$%^&*()-+=_{[]}?~><"

#Put them all together and give your new password a length (increase the length for better security)
string = lower + upper + numbers + symbols
length = 16

#Set the random password using the given values and length in a random order
password = "".join(random.sample(string, length))

#Print our your new, random password
print("Your new password is: " + password)