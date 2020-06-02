from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.template.loader import render_to_string

def index(request):
    context = {}
    
    return render(request, 'index.html', context = context)