#input ->{'temp': 'abc', 'skills': [{'name': '1'}, {'name': '2'}, {'name': '3'}]}
#output required -> {'temp': 'abc', 'skills': {'name': ['1', '2', '3']}}
# list
inp = {'temp': 'abc', 'skills': [{'name': '1'}, {'name': '2'}, {'name': '3'}]}
out = {}
val=[]
for i in inp:
    if i not in out:
        if (type(inp[i]) == list):
            for k in inp[i]:
                ke = next(iter(k))
                val.append(k[ke])
            out[i]= {ke:val}
        else:
            out[i]= inp[i]
    else:
        out[i].extends(inp[i])
print (out)
print (type(out))