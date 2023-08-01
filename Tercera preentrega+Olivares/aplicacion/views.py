from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, "aplicacion/base.html")

def piezaCarro(request):
    return render(request, "aplicacion/piezaCarro.html")

def tipoCarro(request):
    return render(request, "aplicacion/tipoCarro.html")

def profesionales(request):
    return render(request, "aplicacion/profesionales.html")

def planes(request):
    return render(request, "aplicacion/planes.html")

def autoForm(request):
    if request.method == "POST":
        pieza = pieza(nombre=request.POST['nombre'], numero=request.POST['numero'])
        pieza.save()
        return HttpResponse("La pieza a sido agregada correctamente")
    return  render(request, "aplicacion/autoForm.html")

