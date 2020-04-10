
#Shopping App

shoppingList= []
print("Welcome to Shopping app\n")
print("Start entering the items you want and in the end type DONE to quit")

while(1==1):
    item=input()
    if(item!='DONE'):
        shoppingList.append(item)
    else:
        break

print('\nItems present in your shopping list are:')
for item in shoppingList:
    print(item)