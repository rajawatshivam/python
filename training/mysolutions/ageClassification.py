#Age Classification

age = int(input("Enter your age: "))
#version 02
if (age>=60):
    print('You are a Senior Citizen')
elif (age<60 and age>=18):
    print ('You are an adult')
elif (age<18 and age >1):
    print ('Child')
else:
    print('Infant')