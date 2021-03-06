"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app import views
from app.views import home, formEmpresa, empresas, criaProduto, formProduto, produtos, criaEmpresa, produtosEmpresa, \
    pesquisaprodutos, detalheempresa, detalheproduto, excluirempresa, excluirproduto, editarproduto, atualizarproduto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('formempresa/', formEmpresa, name='formEmpresa'),
    path('criaempresa/', criaEmpresa, name='criaEmpresa'),
    path('produtos/', produtos, name='produtos'),
    path('formproduto/', formProduto, name='formProduto'),
    path('criaproduto/', criaProduto, name='criaProduto'),
    path('empresas/', empresas, name='empresas'),
    path('produtosempresa/<int:empresa_id>', produtosEmpresa, name='produtosEmpresa'),
    path('detalheempresa/<int:pk>/', detalheempresa, name='detalheempresa'),
    path('detalheproduto/<int:pk>/', detalheproduto, name='detalheproduto'),
    path('pesquisaprodutos/', pesquisaprodutos, name='pesquisaprodutos'),
    path('excluirempresa/<int:pk>', excluirempresa, name='excluirempresa'),
    path('excluirproduto/<int:pk>', excluirproduto, name='excluirproduto'),
    path('editarproduto/<int:pk>/', editarproduto, name='editarproduto'),
    path('atualizarproduto/<int:pk>/', atualizarproduto, name='atualizarproduto'),
]
