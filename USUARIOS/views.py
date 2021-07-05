from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import *



def registrarse(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            print('ok')
            return HttpResponseRedirect(reverse('login'))
        else:
            print('no ok')
            return HttpResponseRedirect(reverse('registrarse'))

    else:
        print('entro acá')
        form = RegistroForm()
        return render(request, 'registration/registro.html', {
        'form': form
        })