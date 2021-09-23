from django.shortcuts import render, redirect
from app.forms import EmpresaForm, ProdutoForm
from app.models import Empresa, Produto


# Create your views here.
def home(request):
    data = {}
    data['db'] = Empresa.objects.all()
    return render(request, 'index.html', data)


def formEmpresa(request):
    data = {}
    data['form'] = EmpresaForm()
    return render(request, 'formempresa.html', data)


def criaEmpresa(request):
    form = EmpresaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('empresas')


def produtos(request):
    data = {}
    data['banco'] = Produto.objects.all()
    return render(request, 'produtos.html', data)


def formProduto(request):
    data = {}
    data['formproduto'] = ProdutoForm()
    return render(request, 'formproduto.html', data)


def produtosEmpresa(request, idempresa):
    p_lista = Produto.objects.all().filter(empresa=idempresa)
    context = {'produto_lista': p_lista, 'idEmpresa': idempresa}
    return render(request, 'produtosempresa.html', context)


def criaProduto(request):
    formproduto = ProdutoForm(request.POST or None)
    if formproduto.is_valid():
        formproduto.save()
        return redirect('produtos')


def empresas(request):
    data = {}
    data['db'] = Empresa.objects.all()
    return render(request, 'empresas.html', data)


def pesquisaprodutos(request):
    e_lista = Empresa.objects.all()
    context = {'empresa_lista': e_lista}
    return render(request, 'pesquisaprodutos.html', context)
