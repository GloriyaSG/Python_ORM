import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Pet, Artifact, Location


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
    return '\n'.join(str(l) for l in locations)

def new_capital():
    location = Location.objects.first()
    location.is_capital = True
    location.save()

def get_capital():
    return Location.objects.filter(is_capital=True).values('name')

def delete_first_location():

