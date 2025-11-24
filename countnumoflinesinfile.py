#count the number of lines in a file
f=open('sample.txt','r')
count=0
for line in f:
    count+=1
print(count)
f.close()
