from django.forms import ModelForm
from app.models import Empresa, Produto


# Create the form class.
class EmpresaForm(ModelForm):
    class Meta:
        model = Empresa
        fields = ['nome', 'cnpj', 'telefone', 'endereco']

class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'estoque', 'preco', 'status']

