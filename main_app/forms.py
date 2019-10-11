from django import forms
from .models import Segproy

class ProyForm(forms.ModelForm):
    class Meta:
        model = Segproy
        fields = ['rastreo', 'empresa', 'proyecto', 'estatus', 'avance', 'entrega']