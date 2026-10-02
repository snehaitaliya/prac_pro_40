def prime(n):
    cnt=0
    for i in range(1,n+1):
        if n%i==0:
            cnt+=1  
    if cnt<=2:
        print(n,"is prime number.")
    else:
        print(n,"is not prime number.")

n=int(input("Enter number : "))
prime(n)