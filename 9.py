#Count frequency of each character2
s=input("Enter String : ")

for i in s:
    cnt=0
    for j in s:
        if i==j:
            cnt+=1                        

    print(i,"=",cnt,"time")
