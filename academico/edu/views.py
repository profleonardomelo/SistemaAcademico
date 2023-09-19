from time import timezone

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404 # modificado
from .models import Matricula # modificado
from django.utils import timezone


# modificado
#def index(request):
#    return HttpResponse('<h1>Matrículas</h1>')

# modificado

def index(request): # modificado

    matriculas = Matricula.objects.all()

    #dados_dos_institutos = {
    #    'IFBA': 'BAHIA',
    #    'IF Goiano': 'GOIÁS',
    #    'IFSP': 'SÃO PAULO',
    #    'IFMG': 'MINAS GERAIS'
    #}

    dados = {
        'matriculas': matriculas
    }

    return  render(request, 'index.html', dados)

def cadastro(request):
    return render(request, 'cadastro.html')

def edu(request, matricula_id):

    matricula = get_object_or_404(Matricula, pk=matricula_id)

    matricula_a_exibir = {
            'matricula' : matricula,
            'data_acesso' : timezone.now(),
    }

    return render(request, 'matricula.html', matricula_a_exibir)
