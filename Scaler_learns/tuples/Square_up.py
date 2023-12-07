def calc(x):
    p=4*x
    a=x**2
    return p, a

side=int(input())
p,a=calc(side)

print(f"Perimeter: {p}")
print(f"area: {a}")