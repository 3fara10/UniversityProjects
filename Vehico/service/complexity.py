import string
import random

from domain.masina import Masina


def generate_token():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))

def generate_car_object():
    brands = [
        "Chevrolet", "Chevrolet", "Ford", "Volvo", "Toyota",
        "Chevrolet", "Toyota", "Toyota", "Audi", "Ford",
        "Audi", "Audi", "Chevrolet", "Suzuki", "Ford", "Mercedes-Benz",
        "Mercedes-Benz", "BMW", "BMW", "Toyota", "Audi", "Chevrolet",
        "Chevrolet", "Toyota", "BMW", "Ford", "BMW", "Subaru",
        "Toyota", "Chevrolet", "Suzuki", "Ford", "Toyota", "Subaru",
        "Chevrolet", "Ford", "Suzuki", "Audi", "Volvo",
        "Chevrolet", "BMW", "BMW", "Chevrolet", "Mercedes-Benz",
        "Mercedes-Benz", "BMW", "Audi", "Chevrolet", "Chevrolet"
    ]

    models = [
        "Malibu", "Silverado", "Transit", "850", "LandCruiser",
        "Silverado3500HD", "T100", "Avalon", "A8", "Taurus",
        "S7", "RS5", "Cavalier", "SX4", "Econoline", "Mercedes-AMG",
        "E-Class", "M5", "1Series", "Tundra", "A6", "Express2500",
        "Malibu", "Highlander", "X5", "Taurus", "3Series", "Outback",
        "RAV4", "3500RegularCab", "Esteem", "Fiesta", "Mirai", "BRZ",
        "Silverado3500RegularCab", "F150SuperCrewCab", "Sidekick", "A3", "V40",
        "Suburban", "3Series", "5Series", "S10RegularCab", "SLK-Class",
        "CLK-Class", "3Series", "A3", "Malibu", "Silverado"
    ]
    token = generate_token()
    model = random.choice(models)
    marca=random.choice(brands)
    number1 = random.randint(1000, 9999)
    number2 = random.randint(1000, 9999)
    masina=Masina(marca,model,token,number1,number2)
    return masina

def generate_car_objects_list(num_objects):
    car_objects = []
    for _ in range(num_objects):
        car_objects.append(generate_car_object())
    return car_objects

