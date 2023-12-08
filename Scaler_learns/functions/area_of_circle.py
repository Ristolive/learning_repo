def circle_area(r):
    return 3.14159*(r)**2

radius=int(input("Enter Radius: "))
a=circle_area(radius)
print(round(a,2))