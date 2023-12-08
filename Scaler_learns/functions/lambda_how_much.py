price=int(input("Enter the price: "))
perc=int(input("Enter percentage: "))
res=(lambda x,y:x*y/100)(price,perc)
print(res)