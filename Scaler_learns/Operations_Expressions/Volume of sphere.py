def volumeofsphere(radius):
    return (4 * (22 / 7) * (radius) ** 3) / 3


radius = int(input("Enter Radius: "))

result = volumeofsphere(radius)
print(round(result, 2))
