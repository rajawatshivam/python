"""
Name: 
    Clean the Messy salary        
Filename:
    salary.py
Problem Statement:
    Clean the Messy salary into integers for Data Processing
    salary = '$876,001'
    
    Remove the $
    Remove the ,
    Convert the string into integer
Hint: 
    We can use slicing concept to remove $ or remove() method 
    We can use the split and join to remove the , comma
    We can use the int() typecast to convert into integer
"""


salary = '$876,001' 

#Answer
s = salary[1:]          # 
s1 = s.split(',')
s2 = "".join(s1)
s3 = int(s2)
print(s3)
# Using the Chaining Concept
print(int("".join(salary[1:].split(','))))

    

