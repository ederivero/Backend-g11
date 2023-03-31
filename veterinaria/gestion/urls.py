from django.urls import path
from .views import RegistroUsuario, PerfilUsuario, Mascotas
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('registro', RegistroUsuario.as_view()),
    path('login', TokenObtainPairView.as_view()),
    path('perfil', PerfilUsuario.as_view()),
    path('mascotas', Mascotas.as_view()),
]