from django import forms
from .models import Estoque, Categoria

class NovoItemForm((forms.ModelForm)):  
    class Meta:
        model = Estoque
        fields=(
            'nome', 'quantidade', 'preco', 'categoria'
        )

class CategoriaForm((forms.ModelForm)):  
    class Meta:
        model = Categoria
        fields=('nome',)