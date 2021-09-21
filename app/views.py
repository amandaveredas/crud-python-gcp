from django.shortcuts import render, redirect
from app.forms import EmpresaForm
from app.models import Empresa

# Create your views here.
def home(request):
    data = {}
    data['db'] = Empresa.objects.all()
    return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = EmpresaForm()
    return render(request, 'formEmpresa.html', data)

def create (request):
    form = EmpresaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')