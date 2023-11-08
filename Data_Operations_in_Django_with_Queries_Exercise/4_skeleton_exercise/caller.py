import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Pet, Artifact, Location, Car


# Create queries within functions
def create_pet(name:str, species:str):
    pet = Pet.objects.create(
        name=name,
        species=species
    )
    return f"{pet.name} is a very cute {pet.species}!"

# print(create_pet('Buddy', 'Dog'))
# print(create_pet('Whiskers', 'Cat'))
# print(create_pet('Rocky', 'Hamster'))
def create_artifact(name: str, origin: str, age: int, description: str, is_magical: bool):
    artifact = Artifact.objects.create(
        name=name,
        origin=origin,
        age=age,
        description=description,
        is_magical=is_magical
    )
    return f"The artifact {artifact.name} is {artifact.age} years old!"

def delete_all_artifacts():
    Artifact.objects.all().delete()


# print(create_artifact('Ancient Sword', 'Lost Kingdom', 500, 'A legendary sword with a rich history', True))
#
# print(create_artifact('Crystal Amulet', 'Mystic Forest', 300, 'A magical amulet believed to bring good fortune', True))

def show_all_locations():
    locations = Location.objects.all().order_by('-id')
    result = []
    for l in locations.all():
        result.append(f'{l.name} has a population of {l.population}!')
    return '\n'.join(result)

def new_capital():
    location = Location.objects.first()
    location.is_capital = True
    location.save()

def get_capitals():
    return Location.objects.filter(is_capital=True).values('name')

def delete_first_location():
    Location.objects.first().delete()

# print(show_all_locations())
# print(new_capital())
# print(get_capitals())
def apply_discount():
    cars = Car.objects.all()

    for car in cars:
        pr_off = sum(int(x) for x in str(car.year)) / 100
        disc = float(car.price) * pr_off
        car.price_with_discount = float(car.price) - disc
        car.save()

def get_recent_cars():
    return Car.objects.filter(year__gte=2020).values('model', 'price_with_discount')

def delete_last_car():
    Car.objects.last().delete()



