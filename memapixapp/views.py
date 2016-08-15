from django import forms
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.views import login
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required


@login_required(login_url='login/')
def home(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect('/memapixapp/')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {
        'form': form,
    })







