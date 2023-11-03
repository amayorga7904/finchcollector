from django.db import models
from django.urls import reverse

TYPES = (
    ('BUG', 'Bug'),
    ('DRK', 'Dark'),
    ('DRG', 'Dragon'),
    ('ELC', 'Electric'),
    ('FRY', 'Fairy'),
    ('FGT', 'Fighting'),
    ('FIR', 'Fire'),
    ('FLY', 'Flying'),
    ('GHS', 'Ghost'),
    ('GRS', 'Grass'),
    ('GRD', 'Ground'),
    ('ICE', 'Ice'),
    ('NML', 'Normal'),
    ('PSN', 'Poison'),
    ('PSY', 'Psychic'),
    ('RCK', 'Rock'),
    ('STL', 'Steel'),
    ('WTR', 'Water'),
)

# Create your models here.
class Vape(models.Model):
    brand = models.CharField(max_length=50)
    flavor = models.CharField(max_length=50)

    def __str__(self):
        return self.brand

    def get_absolute_url(self):
        return reverse('vapes_detail', kwargs={'pk': self.id})

class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    height = models.IntegerField()
    weight = models.IntegerField()
    level = models.IntegerField()
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    vapes = models.ManyToManyField(Vape)

    def __str__(self):
        return f'{self.name} ({self.id})'  
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pokemon_id': self.id})  
    
class Move(models.Model):
    move_name = models.CharField()
    move_type = models.CharField(
        max_length=3,
        choices=TYPES,
        default=TYPES[12][0]
    )

    pokemon = models.ForeignKey(
        Pokemon,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.move_name} is {self.get_move_type_display()}'
    

class Photo(models.Model):
    url = models.CharField(max_length=200)
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for pokemon_id: {self.pokemon_id} @{self.url}"
