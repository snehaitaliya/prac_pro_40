#Count words in a sentence.
n=input("Enter sentence : ")

cnt=1
for i in n:
    if i==" ":
        cnt+=1
print("Count words : ",cnt)
