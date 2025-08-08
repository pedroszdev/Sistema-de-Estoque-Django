from django.shortcuts import render, redirect
from django.urls import reverse
from SistemaEstoque.forms import CategoriaForm
def add_ctg(request):
    form_action=reverse('SistemaEstoque:nova_categoria')

    if request.method == 'POST':
        form=CategoriaForm(request.POST)

        contexto={
            'form_action':form_action,
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('SistemaEstoque:home')
        
        return render(request, 'SistemaEstoque/nova_ctg.html', contexto)
    
    contexto={
            'form': CategoriaForm(),
            'form_action':form_action,}
    
    return render(request,'SistemaEstoque/nova_ctg.html', contexto)