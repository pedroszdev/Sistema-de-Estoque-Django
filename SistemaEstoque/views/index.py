from django.shortcuts import render
from SistemaEstoque.models import Estoque,Categoria
from django.db.models import Sum, F


def home(request):
    total_categoria=Categoria.objects.count()
    if request.user.is_authenticated:
        total_produtos=Estoque.objects.filter(criador=request.user).count()
        valor_total = Estoque.objects.filter(criador=request.user).aggregate(
                total=Sum(F('quantidade') * F('preco'))
            )['total'] or 0
    else:
        total_produtos= 0
        valor_total = 0

    contexto={
        'total_produtos' : total_produtos,
        'total_categoria' : total_categoria,
        'valor_total' : valor_total
    }
    return render(request,'SistemaEstoque/index.html', contexto)