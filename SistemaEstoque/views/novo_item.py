from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from SistemaEstoque.forms import NovoItemForm
from SistemaEstoque.models import Estoque
from django.contrib.auth.decorators import login_required



@login_required(login_url='SistemaEstoque:login')
def add_item(request):
    form_action=reverse('SistemaEstoque:novo_item')

    if request.method == 'POST':
        form=NovoItemForm(request.POST)

        contexto={
            'form_action':form_action,
            'form': form
        }
        if form.is_valid():
            produto=form.save(commit=False)
            produto.criador= request.user
            produto.save()
            return redirect('SistemaEstoque:inventario')
        
        return render(request, 'SistemaEstoque/novo_item.html', contexto)
    
    contexto={
            'form': NovoItemForm(),
            'form_action':form_action,}
    
    return render(request,'SistemaEstoque/novo_item.html', contexto)



@login_required(login_url='SistemaEstoque:login')
def update(request, id_item):
    estoque= get_object_or_404(Estoque,pk=id_item, criador=request.user)
    form_action=reverse('SistemaEstoque:update', args=(id_item,))
    form = NovoItemForm(instance=estoque)
    if request.method == 'POST':
        form = NovoItemForm(request.POST, instance=estoque )
        contexto={
            'form_action' : form_action,
            'form' : form
        }
        if form.is_valid():
            estoque=form.save()

            return redirect('SistemaEstoque:inventario')
    
    contexto={
            'form_action' : form_action,
            'form' : form
        }

    return render(request, 'SistemaEstoque/update.html', contexto)



@login_required(login_url='SistemaEstoque:login')
def delete(request, id_item):
    item= Estoque.objects.get(id=id_item, criador=request.user)
    item.delete()
    return render(request,'SistemaEstoque/inventario.html')