#Check if a string is a palindrome.
s=input("Enter String : ")

if s== s[::-1]:
    print("String is Palindrome")
else:
    print("String is not Palindrome")