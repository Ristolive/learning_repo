contacts= (
    ("James", 42),
    ("Amy", 24),
    ("John", 31),
    ("Amanda", 63),
    ("Bob", 18)
)
name=input("Enter name: ")
for contact in contacts:
    if contact[0]==name.capitalize():
        print(f"{name.capitalize()} is {contact[1]}")
        break
else:
    print(f"{name.capitalize()} Not Found")

