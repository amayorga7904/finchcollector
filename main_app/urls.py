from django.urls import path
from . import views
	
urlpatterns = [
	path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pokemon/', views.pokemons_index, name='index'),
    path('pokemon/<int:pokemon_id>/', views.pokemon_detail, name='detail'),
    path('pokemon/create/', views.PokemonCreate.as_view(), name='pokemons_create'),
    path('pokemon/<int:pk>/update/', views.PokemonUpdate.as_view(), name='pokemons_update'),
    path('pokemon/<int:pk>/delete/', views.PokemonDelete.as_view(), name='pokemons_delete'),
]