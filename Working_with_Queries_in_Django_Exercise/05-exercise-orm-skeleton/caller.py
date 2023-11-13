import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
from main_app.models import ArtworkGallery
# Create and check models
def show_highest_rated_art():
    art = ArtworkGallery.objects.order_by('-rating', 'id').first()
    return f'{art.art_name} is the highest-rated art with {art.rating} rating!'

def bulk_create_arts(first_art, second_art):
    ArtworkGallery.objects.bulk_create([
        first_art,
        second_art,
    ])

def delete_negative_rated_arts():
    ArtworkGallery.objects.filter(rating__lt=0).delete()


# Run and print your queries
# artwork1 = ArtworkGallery(artist_name="Vincent van Gogh", art_name="Starry Night", rating=4, price=1200000.0)
# artwork2 = ArtworkGallery(artist_name="Leonardo da Vinci", art_name="Mona Lisa", rating=5, price=1500000.0)
#
# # Bulk saves the instances
# bulk_create_arts(artwork1, artwork2)
# print(show_highest_rated_art())
# print(ArtworkGallery.objects.all())

