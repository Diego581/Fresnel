from django.shortcuts import render
from formula import fresnel
from django.http import HttpResponse

# MainPage

def index(request):
    return render(request, 'app/index.html', {'resultado': " "})
    

def calculadora(request):
    km = request.GET['query']
    try:
        GHz = request.GET['frecuencia']
    except:
        return render(request, 'app/index.html', {'error': 'Insert a frequency value'})
    try:   
        resultado = fresnel(km,GHz)
        resultado = str(resultado) + " Metros"
        return render(request, 'app/index.html', {'resultado' : resultado}) 
    except:
        return render(request, 'app/index.html') 
 

   