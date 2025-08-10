from django.shortcuts import render
from SistemaEstoque.models import Estoque,Categoria
from django.db.models import Sum, F
from django.contrib.auth.decorators import login_required


@login_required(login_url='SistemaEstoque:login')
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