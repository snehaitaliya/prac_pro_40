l={"A":50,"B":90,"C":70,"D":80}

max=0
max_key=""

for key in l:
    if l[key]>max:
        max=l[key]
        max_key=key
print("key with max value : ",max_key)
print("max value : ",max)