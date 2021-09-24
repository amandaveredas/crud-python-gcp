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
    e_lista = Empresa.objects.all().order_by('nome')
    context = {'empresa_lista': e_lista}
    return render(request, 'pesquisaprodutos.html', context)


def produtosEmpresa(request, empresa_id):
    p_lista = Produto.objects.all().filter(empresa=empresa_id)
    nome_empresa = Empresa.objects.get(pk=empresa_id)
    context = {'produto_lista': p_lista, 'empresa_id': empresa_id, "nome_empresa": nome_empresa}
    return render(request, 'produtosempresa.html', context)


def detalheempresa(request, pk):
    data = {}
    data['db'] = Empresa.objects.get(pk=pk)
    return render(request, 'detalheempresa.html', data)


def detalheproduto(request, pk):
    data = {}
    data['db'] = Produto.objects.get(pk=pk)
    return render(request, 'detalheproduto.html', data)


def excluirempresa(request, pk):
    Empresa.objects.get(pk=pk).delete()
    return redirect('empresas')


def excluirproduto(request,pk):
    Produto.objects.get(pk=pk).delete()
    return redirect('produtos')
