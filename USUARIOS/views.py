from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import *



def registrarse(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('login'))
        else:
            return HttpResponse('no es válido gato')

    else:
        form = RegistroForm()
        return render(request, 'registration/registro.html', {
        'form': form
        })