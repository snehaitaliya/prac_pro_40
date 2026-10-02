#Copy contents from one file to another

f=open("file1.txt","r")
f1=open("file2.txt","w")

for i in f:
    f1.write(i)

f.close()
f1.close()