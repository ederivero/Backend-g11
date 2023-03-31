from django.urls import path
from .views import RegistroUsuario

urlpatterns = [
    path('registro', RegistroUsuario.as_view()),
]