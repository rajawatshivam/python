#lambda
#map
#tumple


list2 = [1,2,3,4,5]

def f1(x):
    return x**3

f1(list2[0])


#map take 2 parameters
list(map(f1 , list2))

#output of map needs to be typecasted that's why we changed it to list
list3= ['amar','akbar','anthony']

def f2(str1):
    return len(str1)

list(map(f2, list3))

#lambda #takes input before colon and output after colon
#it is anonymous function
list(map(lambda str1:len(str1+str1), list3))

list(map(lambda x:x**3, list2))


list5 =[10,20,30,40,50]

def f3(x):
    return x+1

list(map(f3,list5))

list(map(lambda x:x+1, list5))

list6 = [10,3,5,6,81,11]
def f4(x):
    if(x>10):
        return True
    else:
        return False

#list(map(f4,list6))
#filter only return values for which function returns true
list(filter(f4,list6))

list7=['Jaipur','Kota','alvar','bikaner','Udaipur']
def f5(x):
    if(x[0].isupper()):
        return True
    else:
        return False

def f6(x):
    return 'pur' in x

list(filter(f5,list7))

list(filter(lambda x:'pur' in x, list7))


#reduce
#you have to import functools

import functools

list8=[1,2,3,4,5,6,7,8,9,10]

def f7(x,y):
    return x+y

functools.reduce(f7,list8)


#tuple
tuple1=(1,2,3,5)
type(tuple1)

tuple1.index(3)

tp2=(3,)
type(tp2)
        

tp3=(3)
type(tp3)