from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import Segproy
from .forms import ProyForm
from django.contrib.auth import authenticate

# Create your views here.
def index (request):
    
    return render(request, 'index.html')

def rastrear (request, rastreo):
    form = ProyForm(request.GET)
    rastreo = Segproy.objects.get(id = rastreo)
    return render(request, 'rastrear.html', {'form':form})
    #if request.method == 'POST':
    # si fue un POST entonces autenticamos el rastreo con la base de datos
        #form = ProyForm()
        #rastreo = request.POST['rastreo']
        #ra = authenticate(rastreo = rastreo)
        #if ra is not None:
            #return render(request, 'rastrear.html', {'form':form})
        #else:
            #print("No se encuentra registro")
            #return HttpResponseRedirect('index.html')
    #else:
        # si no es un POST simplemente desplegamos index

        #return HttpResponseRedirect('index.html')