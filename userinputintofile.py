#take input from user and write it in file
s=input("enter any strng of  sentence")
f=open('user.txt','w+')
f.write(s)
f.seek(0)
data=f.read()
print(data)
f.close()
