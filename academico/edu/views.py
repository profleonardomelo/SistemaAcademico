from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render # modificado

# modificado
#def index(request):
#    return HttpResponse('<h1>Matrículas</h1>')

# modificado

dados_dos_institutos = {
    'IFBA' : 'BAHIA',
    'IF Goiano' : 'GOIÁS',
    'IFSP' : 'SÃO PAULO',
    'IFMG' : 'MINAS GERAIS'
}

dados = {
    'dados_dos_institutos' : dados_dos_institutos
}

def index(request): # modificado
    return  render(request, 'index.html', dados)

def cadastro(request):
    return render(request, 'cadastro.html')
