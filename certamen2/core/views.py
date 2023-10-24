from django.shortcuts import render
from django.http import HttpResponse
from .models import Entidad,Comunicado
def index(request):
    titulo      = "inicio"
    comunicados = Comunicado.objects.all()
    entidades   = Entidad.objects.all()
    data = {
        "titulo":titulo,
        "comunicados":comunicados,
        "entidades":entidades
    }
    
    return render(request,'core/index.html',data)

# Create your views here.
