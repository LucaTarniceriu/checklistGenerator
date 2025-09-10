from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('revizie/', views.revizie, name='revizie'),
    path('magazin/', views.magazin, name='magazin'),
    path('adaugaUsa/', views.addDoor, name='adaugaUsa'),
    path('deleteSite/', views.deleteSite, name='deleteSite'),
    path('magazinRedirect/', views.magazinRedirect, name='magazinRedirect'), #to redirect to "magazin" with context data
    path('deleteDoor/', views.deleteDoor, name='deleteDoor'),
    path('export/', views.export, name='pdfExport')
]