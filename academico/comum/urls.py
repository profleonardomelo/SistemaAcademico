from django.urls import path # modificado
from . import views # modificado

# modificado
urlpatterns = [
    path('cadastro', views.cadastro, name='cadastro'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('login', views.login, name='login'),
    path('logout', views.dashboard, name='logout'),
]