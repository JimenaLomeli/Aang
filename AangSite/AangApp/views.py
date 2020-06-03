from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
# from .forms import codigo
import subprocess
from subprocess import call
from django import forms
import pickle as pickle


@csrf_exempt
def index(request):
    context = {}
    try:
        with open("MatColors.pickle", "rb") as f:
            context = pickle.load(f)
    except:
        print("No funciono pickle")

    class codigos(forms.Form):
        code = open('input.txt', 'r')
        content = code.read()
        code.close()

        codigoText = forms.CharField(
            widget=forms.Textarea, initial=str(content))
    form = codigos()
    if request.method == 'POST':
        form = codigos(request.POST)
        if form.is_valid():
            code = form.cleaned_data['codigoText']
            code = code.replace('\r', '')
            f = open('input.txt', 'w')
            f.write(code)
            f.close()
            inp = "./inputFile.txt"
            call(["python", "C:/Users/Jorge Andres Sabella/Aang/Grammar/AangMain.py",
                  "C:/Users/Jorge Andres Sabella/Aang/AangSite/input.txt"])
            call(
                ["python", "-u", "C:/Users/Jorge Andres Sabella/Aang/Grammar/VirtualMachine.py"])
            return redirect('/')
            # call(
            #    ["python", "C:/Users/Jorge Andres Sabella/Aang/AangSite/test.py"])
            # context = {
            #     'color1': 'red',
            #     'color2': 'blue',
            #     'color3': 'red',
            #     'color4': 'green',
            #     'color39': 'black',
            #     'color41': 'black'
            # }

    context['codigo'] = form
    return render(request, 'index.html', context=context)
