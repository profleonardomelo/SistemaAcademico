from django.contrib import admin
from .models import Matricula

# Register your models here.
class AdminMatricula(admin.ModelAdmin):
    list_display = ('id', 'matricula', 'aluno', 'curso', 'observacao', 'data_matricula')
    list_display_links = ('id', 'matricula', 'aluno', 'curso', 'observacao', 'data_matricula')
    search_fields = ('id', 'matricula', 'aluno__user__first_name', 'curso', 'observacao', 'data_matricula')
    list_filter = ('curso',)
    list_per_page = 10


admin.site.register(Matricula, AdminMatricula)


