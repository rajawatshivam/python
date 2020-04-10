#file handling

fp = open('D:/Users/O46658/Desktop/wo.txt','r')
print(fp.read())
fp.close()

#readline
print(fp.readline())

#write
fp =open('newfile.txt','w')
fp.write("hi blah lbah")
fp.close()


