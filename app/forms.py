from django.forms import ModelForm
from app.models import Empresa

# Create the form class.
class EmpresaForm(ModelForm):
    class Meta:
        model = Empresa
        fields = ['nome', 'cnpj', 'telefone', 'endereco']

