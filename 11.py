#Find common elements between two lists.

l=[3,4,5,6,7]
l1=[5,6,7,8,9]

for i in l:
    for j in l1:
        if i==j:
            print(i)