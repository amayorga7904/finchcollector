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
class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    height = models.IntegerField()
    weight = models.IntegerField()
    level = models.IntegerField()
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    def __str__(self):
        return f'{self.name} ({self.id})'  
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pokemon_id': self.id})  
    
class Move(models.Model):
    move_name = models.CharField()
    move_type = models.CharField(
        max_length=3,
        choices=TYPES
    )

    pokemon = models.ForeignKey(
        Pokemon,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.get_move_type_display()} on {self.move_name}'