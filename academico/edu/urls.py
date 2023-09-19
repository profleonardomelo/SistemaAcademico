from django.urls import path # modificado
from . import views # modificado

# modificado
urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('<int:matricula_id>', views.edu, name='edu'),
]