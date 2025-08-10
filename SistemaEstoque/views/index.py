from django.shortcuts import render
from SistemaEstoque.models import Estoque,Categoria
from django.db.models import Sum, F
def home(request):
    total_produtos=Estoque.objects.count()
    total_categoria=Categoria.objects.count()
    valor_total = Estoque.objects.aggregate(
            total=Sum(F('quantidade') * F('preco'))
        )['total'] or 0

    contexto={
        'total_produtos' : total_produtos,
        'total_categoria' : total_categoria,
        'valor_total' : valor_total
    }
    return render(request,'SistemaEstoque/index.html', contexto)