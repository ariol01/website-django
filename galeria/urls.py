from django.urls import path
from galeria.views import imagem, index
from galeria.views import teste


urlpatterns = [
     path('', index, name='index'),
     path('', teste),
     path('imagem/', imagem, name='imagem')
]