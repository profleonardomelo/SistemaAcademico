from django.urls import path # modificado
from . import views # modificado

# modificado
urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro', views.cadastro, name='cadastro')
]