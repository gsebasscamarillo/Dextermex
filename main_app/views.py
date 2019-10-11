from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import Segproy
from .forms import ProyForm
from django.contrib.auth import authenticate

# Create your views here.
def index (request):
    return render(request, 'index.html')

def rastrear (request):
    if request.method == 'POST':
        form = ProyForm(request.POST)
        rastreo = request.POST['rastreo']
        proyecto = Segproy.objects.get(rastreo = rastreo)
        return render(request, 'rastrear.html', {'proyecto' : proyecto})