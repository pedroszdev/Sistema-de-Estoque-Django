from django.shortcuts import render, redirect
from django.urls import reverse
from SistemaEstoque.forms import CategoriaForm
from django.contrib.auth.decorators import login_required


@login_required(login_url='SistemaEstoque:login')
def add_ctg(request):
    form_action=reverse('SistemaEstoque:nova_categoria')

    if request.method == 'POST':
        form=CategoriaForm(request.POST)

        contexto={
            'form_action':form_action,
            'form': form
        }
        if form.is_valid():
            categoria=form.save(commit=False)
            categoria.criador= request.user
            categoria.save()
            return redirect('SistemaEstoque:inventario')
        
        return render(request, 'SistemaEstoque/nova_ctg.html', contexto)
    
    contexto={
            'form': CategoriaForm(),
            'form_action':form_action,}
    
    return render(request,'SistemaEstoque/nova_ctg.html', contexto)