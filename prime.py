n=int(input("enter the number "))
prime=True
for i in range(2,n):
    if(n%i==0):
        prime=False
        break
if prime:
    print("prime",n)
else:
    print("not prime",n)


