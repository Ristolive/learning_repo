car={
    "brand": "BMW",
    "year": 2018,
    "color": "red",
    "mileage": 15000
}
enter=input("Enter details: ")
i=car.get(enter.lower(), "Not found")
print(i)