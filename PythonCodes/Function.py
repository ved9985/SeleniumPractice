
cars = [
    {"name" : "Nano", "model" : "Base", "mileage":100, "fuel_consumed": 1},
    {"name" : "Tiago", "model" : "Advance", "mileage":75, "fuel_consumed": 2},
    {"name" : "Breeza", "model" : "Automated", "mileage":50, "fuel_consumed": 3},
    {"name" : "Range Rover", "model" : "Super Model", "mileage":25, "fuel_consumed": 4}
    ]
def calculate_mileage(car):

    mpg = car["mileage"]/car["fuel_consumed"]
    return mpg
def name_info(car):
    name = f"{car['name']} is of {car['model']} mototadel"
    return name
def full_info():
    x = calculate_mileage(car)
    y= name_info(car)
    print(f"{x} and have {y} Km/Ltr !")

for car in cars:
    full_info()
