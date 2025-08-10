from django.shortcuts import render, get_object_or_404
from SistemaEstoque.models import Estoque
from django.contrib.auth.decorators import login_required


@login_required(login_url='SistemaEstoque:login')
def item_sozinho(request, id_item):
    item= Estoque.objects.get(id=id_item)
    contexto={
        'item': item,
    }
    return render(request, 'SistemaEstoque/item_sozinho.html', contexto)