from django.contrib import admin
from .models import Aluno

# Register your models here.

class AdminAluno(admin.ModelAdmin):
    list_display = ('id', 'user', 'email', 'data_nascimento', 'sexo', 'telefone')
    list_display_links = ('id', 'user', 'email', 'data_nascimento', 'sexo', 'telefone')
    list_filter = ('sexo',)
    list_per_page = 10

admin.site.register(Aluno, AdminAluno)

