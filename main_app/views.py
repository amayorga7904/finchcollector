from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Pokemon
# Create your views here.


def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def pokemons_index(request):
  pokemons = Pokemon.objects.all()
  return render(request, 'pokemon/index.html', {
    'pokemons': pokemons
  })

def pokemon_detail(request, pokemon_id):
  pokemon = Pokemon.objects.get(id=pokemon_id)
  return render(request, 'pokemon/detail.html', {
    'pokemon': pokemon
  })

class PokemonCreate(CreateView):
  model = Pokemon
  fields = '__all__'

class PokemonUpdate(UpdateView):
  model = Pokemon
  fields = ['weight', 'level', 'description', 'age']

class PokemonDelete(DeleteView):
  model = Pokemon
  success_url = '/pokemon' 