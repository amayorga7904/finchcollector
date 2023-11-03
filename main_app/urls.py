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
    path('pokemon/<int:pokemon_id>/add_move/', views.add_move, name='add_move'),

    path('pokemon/<int:pokemon_id>/add_photo/', views.add_photo, name='add_photo'),

    path('vapes/', views.VapeList.as_view(), name='vapes_index'),
    path('vapes/<int:pk>/', views.VapeDetail.as_view(), name='vapes_detail'),
    path('vapes/create/', views.VapeCreate.as_view(), name='vapes_create'),

    # associate a toy with a cat (M:M)
    path('pokemon/<int:pokemon_id>/assoc_vape/<int:vape_id>/', views.assoc_vape, name='assoc_vape'),
    path('pokemon/<int:pokemon_id>/unassoc_vape/<int:vape_id>/', views.unassoc_vape, name='unassoc_vape'),
]