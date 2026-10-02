#Rotate a list by N positions.
l=[1,2,3,4,5]
n=int(input("Enter N : "))

n=n%len(l)
l1=l[n:]+l[:n]
print("Rotated list : ",l1)
      
            
            