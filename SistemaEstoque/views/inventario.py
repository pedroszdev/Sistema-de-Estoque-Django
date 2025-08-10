from django.shortcuts import render
from SistemaEstoque.models import Estoque,Categoria
from django.core.paginator import Paginator
from django.db.models import Q


def inventario(request):
    estoque=Estoque.objects.filter().order_by('-id',)
    paginator=Paginator(estoque,30)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    
    contexto={
        'estoque':page_obj
    }



    return render(request,'SistemaEstoque/inventario.html',contexto)

def search(request):
    search_value=request.GET.get('q', '').strip() 
    
    estoque=Estoque.objects.filter(
        Q(nome__icontains=search_value) | 
        Q(quantidade__icontains=search_value) | 
        Q(id__icontains=search_value) |
        Q(preco__icontains=search_value) 
        )\
    .order_by('-id',)
    
    paginator=Paginator(estoque, 30)
    
    page_number= request.GET.get('page')
    
    page_obj= paginator.get_page(page_number)

    contexto={
        'search_value' :search_value,
        'estoque': page_obj,
    }

    return render(request, 'SistemaEstoque/inventario.html', contexto)

