n = int(input())

for i in range(n):
    print("*" * (i+1) + " " * (2*n-2*i-2) + "*" * (i+1))

for i in range(n):
    print("*" * (n-i-1) + " " * 2*(1+i) + "*" * (n-i-1))

print()

for i in range(n):
    if i==0:
        print("*" * n)
    elif i<(n-1):
        print("*" + " " * (n-i-2) + "*")
    else:
        print("*")

print()

for i in range(n):
    if i<=1:
        print(" " * (n-i-1) + "*" * (i+1))
    else:
        print(" " * (n-i-1) + "*" + " " * (i-1) + "*")
for i in range(n):
    if i>=n-3:
        print(" " * (i+1) + "*" * (n-i-1))
    else:
        print(" " * (i+1) + "*" + " " * (n-3-i) + "*")

print()

for i in range(n):
    print(" " * (n-i-1), end="")
    for j in range(1, i+2):
        print(j, end="")
    for k in range(i+1, 1, -1):
        print(k-1, end="")
    print()

print()

for i in range(n):
    print(" " * (n-i-1), end="")
    for j in range(0, i+1):
        print(n-j, end="")
    for j in range(i):
        print(n-i+j+1, end="")
    print()

for i in range(n):
    print(" " * (i+1), end="")
    for j in range(n-i-1):
        print(n-j, end="")
    for j in range(n-i-2):
        print(3+i+j, end="")
    print()

for i in range(n):
    print(" " * (n-i-1), end="")
    for j in range(i+1):
        print((j+1), end="")
    print()

print()

for i in range(n):
    for j in range(i+1):
        print(n-j, end="")
    print(" " * (2*n-3-2*i), end="")
    if i==(n-1):
        for j in range(i):
            print(n-i+j+1, end="")
    else:
        for j in range(i+1):
            print(n-i+j, end="")
    print()
print()

for i in range(n):
    print(" " * (n-i-1), end="")
    for j in range(i+1):
        print(chr(65+j), end="")
    print()
print()

for i in range(n):
    for j in range(n-i):
        print(i+j+1, end=" ")
    for j in range(i):
        print(n-1-j, end=" ")
    print()

print()

for i in range(n):
    print(" " * (n-i-1), end="")
    for j in range(2*i+1):
        if j%2==0:
            print(i+1, end="")
        else:
            print("*", end="")
    print()
for i in range(n-1):
    print(" " * (i+1), end="")
    for j in range(2*n-2*i-3):
        if j%2==0:
            print(n-i-1, end="")
        else:
            print("*", end="")
    print()
    
print()

for i in range(n):
    for j in range(n):
        if j%2!=0:
            print(chr(65+n-i-1), end="")
        else:
            print(chr(65+i), end="")
    print()
print()

#4.1

for i in range(n):
    if i%2==0:
        for j in range(n):
            print(chr(65+j), end="")
        print()
    else:
        for j in range(n):
            print(j+1, end="")
        print()
        
print()

d = 1

for i in range(n):
    if i==n-1:
        for j in range(i):
            print("*" + str((i+1) * (i+1 + 1) // 2 - j), end="")
        print("*", end="")
    else:
        for j in range(i+1):
            print("*" + str((i+1) * (i+1 + 1) // 2 - j), end="")
    print(" " * (2*n-2*i-3), end="")
    print(" " * (2*n-2*i-2), end="")
    for j in range(i+1):
        print(str(d) + "*", end="")
        d+=1
    print()
