from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from .forms import codigo
from subprocess import call

@csrf_exempt
def index(request):
    context = {}
    if request.method == 'POST':
        form = codigo(request.POST)
        if form.is_valid():
            code = form.cleaned_data['codigoText']
            print(code)
            f = open('input.txt', 'w')
            f.write(code)
            f.close()
            inp = "./inputFile.txt"
            call(["Python3", "/Users/jime/Desktop/Aang/Grammar/AangMain.py", "/Users/jime/Desktop/Aang/AangSite/input.txt"])
            call(["Python3", "/Users/jime/Desktop/Aang/Grammar/VirtualMachine.py"])
            context = {           
                'color1' : 'red',
                'color2' : 'blue',
                'color3' : 'red',
                'color4' : 'green'
            }


    form = codigo()
    context['codigo'] = form




    return render(request, 'index.html', context = context)



