"""
Name: 
    Clean the Messy salary from list        
Filename:
    salary2.py
Problem Statement:
    salaries = ['$876,001', '$543,903', '$2453,896'] 
    Clean the Messy salaries into integers for Data Processing
    Remove the $
    Remove the ,
    Convert into integer
Hint: 
    We can use slicing concept to remove $ or remove() method 
    We can use the split and join to remove the , comma
    We canuse the int() typecast to convert into integer
"""



# version 1
salaries = ['$876,001', '$543,903', '$2453,896'] 
new_salaries=[]

for salary in salaries:
    s = salary[1:]
    s1 = s.split(',')
    s2 = "".join(s1)
    s3 = int(s2)
    new_salaries.append(s3)
    # Using the Chaining Concept
    #new_salaries.append(int("".join(salary[1:].split(','))))
print(new_salaries)    




# version 2
salaries = ['$876,001', '$543,903', '$2453,896'] 
new_salaries=[]

for salary in salaries:
    new_salaries.append(int("".join(salary[1:].split(','))))

print(new_salaries)    
    

