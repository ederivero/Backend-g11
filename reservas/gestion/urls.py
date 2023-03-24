from django.urls import path
from .views import PruebaView

# urlpatterns > NOMBRE OBLIGATORIO para definir nuestras rutas
urlpatterns = [
    path('prueba', PruebaView.as_view()),
    path('otra_prueba', PruebaView.as_view()),
]