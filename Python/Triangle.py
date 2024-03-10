# Program to Draw triangle with user input 
# EG 5
# *
# * * 
# * * *
# * * * *
# * * * * *

#Gettting user input
length = int(input())
#variable to store length of each line
len = 0;
for i in range(length):
    len = len +1 
    for i in range(len):
        print ("* ", end="")
    print("\n")