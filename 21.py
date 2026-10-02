#A Number System Conversion Program is a Python program used to convert numbers from one number system to another, such as binary, decimal, octal, and hexadecimal.

print("1.Decimal to Binary")
print("2.Decimal to Octal")
print("3.Decimal to Hexadecimal")
print("4.Binary to Decimal")
print("5.Binary to Octal")
print("6.Binary to Hexadecimal")
print("7.Octal to Decimal")
print("8.Octal to Binary")
print("9.Octal to Hexadecimal")
print("10.Hexadecimal to Decimal")
print("11.Hexadecimal to Binary")
print("12.Hexadecimal to Octal")

choice=int(input("Enter your choice : "))
num=input("Enter the number : ")

if choice==1:
    print("Binary:",bin(int(num))[2:])

elif choice==2:
    print("Octal:",oct(int(num))[2:])

elif choice==3:
    print("Hexadecimal:",hex(int(num))[2:].upper())

elif choice==4:
    print("Decimal:",int(num, 2))

elif choice==5:
    print("Octal:",oct(int(num, 2))[2:])

elif choice==6:
    print("Hexadecimal:",hex(int(num, 2))[2:].upper())

elif choice==7:
    print("Decimal:",int(num, 8))

elif choice==8:
    print("Binary:",bin(int(num, 8))[2:])

elif choice==9:
    print("Hexadecimal:",hex(int(num, 8))[2:].upper())

elif choice==10:
    print("Decimal:",int(num, 16))

elif choice==11:
    print("Binary:",bin(int(num, 16))[2:])

elif choice==12:
    print("Octal:",oct(int(num, 16))[2:])

else:
    print("Invalid Choice.")
    
