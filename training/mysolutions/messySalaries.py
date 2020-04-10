#Messy Salaries 

salaries = ['$876,001', '$543,903', '$2453,896']
k=0
for item in salaries:
   salaries[k]= item.replace('$','')
   salaries[k] =item.replace('$','')
   k=k+1
    

print (salaries)