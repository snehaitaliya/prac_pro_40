#find longest word in a sentence

s=input("Enter String : ")

words=s.split()
l=""
for word in words:
    if len(word)>len(l):
        l=word

print("Longest word : ",l)