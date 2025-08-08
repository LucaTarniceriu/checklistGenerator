from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('revizie/', views.revizie, name='revizie'),
    path('magazin/', views.magazin, name='magazin'),
    path('adaugaUsa/', views.addDoor, name='adaugaUsa')
]