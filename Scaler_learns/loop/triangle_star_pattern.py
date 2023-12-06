n=int(input("Enter Row: "))

for i in range(1,n+1):
    for x in range(n-i):
        print(" ", end=" ")
    for x in range(2*i-1):
        print("*", end=" ")
    print("\n", end="")