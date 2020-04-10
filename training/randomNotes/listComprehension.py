#list comprehension

[item*item for item in list1]


list1=[10,2,10,4,2,6,7]
list2 = [item*item for item in list1]
print (list2)


list3= ['amar','akbar','anthony']
list4=[len(item) for item in list3]
print (list4)
