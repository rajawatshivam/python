#list

newList = []
type(newList)

newList = [1,2,4,17,305,17]
len(newList)

newList[0] #1
newList[-1] #305

newList[0:4]

#find position of a index of a number or any stored value
#it will only fetch the first number that matches 
newList.index(17)  

#list can be altered unlike string
newList[0]=100
print(newList)

for item in newList: 
    print(item)
    
#append in list
list2=[10,13,4,2,5,6,10]
list2.append(70)
print(list2)

#insert is used to insert value at particular index
list2.insert(4,20)
print(list2)


#clear list
list2.clear()
print(list2)

#remove value from a list
list2 = [10,2,3,4,57,80]
list2.remove(57)
print(list2)

#concatenate two list
list3=list2+newList
print (list3)

#concatenate two list in a existing list
list2.extend(newList)
print (list2)


#pop on list
list2.pop()
list2.pop()
#pop at a specific index
list2.pop(0)

#sorting
list3.sort()
print (list3)
list3.sort(reverse=True)
print(list3)


#list can be hetrogenious
list1 = [10, 'India', True, 3.5]


list1= [10,20,10,7,14,7,10,20,60,75]

while 10 in list1:
    list1.remove(10)
    
print(list1)  
val=list1.count(20)

for x in list1:
    list1.remove(20)
    val=val-1
    if(val==0):
        break
    
print(list1)

