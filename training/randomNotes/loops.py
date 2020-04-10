#control flow
#if, else, elif

mark = 50
#version 01
if (mark>=33):
    print('Pass')
    print ('Congrats')
else: 
    print('Fail')
    print('Better luck next time')
    
    
marks = int(input("Enter the marks: "))
#version 02
if (marks>=60):
    print('First Division')
elif (mark<60 and marks>=45):
    print ('Second Division')
elif (marks<45 and marks >=33):
    print ('Third Division')
else:
    print('Fail')
    
    
#loops
#while, for
    
number = 0
while(number<10):
    number=number+1
    print(number)
    
#for loop   
list1= ['Ram','Sita','Laksman']
for name in list1:
    print (name)
    
    
#break
    
newNum=0
while (newNum<10):
    newNum=newNum+1
    if(newNum==5):
        break
    print(newNum)
    

#continue
newNum=0
while (newNum<10):
    newNum=newNum+1
    if(newNum==5):
        continue
    print(newNum)
    
 