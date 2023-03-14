from django.db import models
import uuid


# Models for the Menu
class Menu(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField()
    sauces = models.CharField(max_length=100)
    ingredients = models.TextField()
    image_1 = models.ImageField(upload_to='images/food/')
    image_2 = models.ImageField(upload_to='images/food/')
    image_3 = models.ImageField(upload_to='images/food/')
    image_4 = models.ImageField(upload_to='images/food/')
    # SAUCES_AVAILABLE_CHOICES = [
    #     ('Tomato Ketchup', 'Tomato Ketchup'),
    #     ('Peri Peri Mayo', 'Peri Peri Mayo'),
    #     ('Shito', 'Shito'),
    #     ('Honey Mustard Mayo', 'Honey Mustard Mayo'),
    #     ('Mango Mayo', 'Mango Mayo'),
    #     ('Only The Brave Hot Sauce', 'Only The Brave Hot Sauce'),
    #     ('Shata Mayonnaisse', 'Shata Mayonnaisse')
    # ]
    # sauces_available = models.CharField(max_length=40, choices=SAUCES_AVAILABLE_CHOICES, default='Tomato Ketchup')

    def __str__(self):
        return self.name
