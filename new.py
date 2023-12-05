row=int(input("Enter Row: "))
col=int(input("Enter columns: "))
sym=input("Enter symbol: ")

for i in range(row):
    for x in range(col):
        print(sym, end=" ")
    print()