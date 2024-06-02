print("right triangle reverse loop")
rows=6
for i in range(1,rows):
    num=1
    for j in range(rows,0,-1):
        if (j>i):
            print(" ",end=" ")
        else:
            print("*",end=" ")
            num+=1
    print()

print("right triangle")
n=6
for i in range(n):
    for  j in range(n-i-1):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()

print("square pattern")
n=5
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()

    
