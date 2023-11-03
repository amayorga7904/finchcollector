from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Pokemon, Vape
from .forms import MoveForm

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
  id_list = pokemon.vapes.all().values_list('id')
  vapes_pokemon_doesnt_have = Vape.objects.exclude(id__in=id_list)
  move_form = MoveForm()
  return render(request, 'pokemon/detail.html', {
    'pokemon': pokemon,
    'move_form': move_form,
    'vapes': vapes_pokemon_doesnt_have
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

def add_move(request, pokemon_id):
  form = MoveForm(request.POST)
  if form.is_valid():
    new_move = form.save(commit=False)
    new_move.pokemon_id = pokemon_id
    new_move.save()
  return redirect('detail', pokemon_id=pokemon_id)

class VapeList(ListView):
  model = Vape

class VapeDetail(DetailView):
  model = Vape

class VapeCreate(CreateView):
  model = Vape
  fields = '__all__'

def assoc_vape(request, pokemon_id, vape_id):
  # Note that you can pass a toy's id instead of the whole toy object
  Pokemon.objects.get(id=pokemon_id).vapes.add(vape_id)
  return redirect('detail', pokemon_id=pokemon_id)

def unassoc_vape(request, pokemon_id, vape_id):
  Pokemon.objects.get(id=pokemon_id).vapes.remove(vape_id)
  return redirect('detail', pokemon_id=pokemon_id)