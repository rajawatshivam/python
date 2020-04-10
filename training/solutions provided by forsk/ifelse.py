"""
Name: 
    Senior Citizen          
Filename:
    ifelse.py
Problem Statement:
    Take the age as input from the user
    print whether he is a infant, Child, Adult,  Senior Citizen
Hint: 
    > 0  and <=1   is Infant
    > 1  and <=18  is Child 
    > 18 and <= 60 is Adult
    > 60 then it   is Senior Citizen
"""

age = float(input("Enter the age: "))
    

if (age > 0 and age <= 1):
    print ("Infant")
elif (age > 1 and age <= 18):
    print ("Child")
elif (age > 18 and age <= 60):
    print ("Adult")
else:
    print ("Senior Citizen")