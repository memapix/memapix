from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.views import login
from django.contrib.auth.decorators import login_required


@login_required(login_url='login/')
def home(request):
    return render(request, 'index.html')







