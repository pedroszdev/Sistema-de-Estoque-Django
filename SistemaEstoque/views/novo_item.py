from django.shortcuts import render, redirect
from django.urls import reverse
from SistemaEstoque.forms import NovoItemForm
def add_item(request):
    form_action=reverse('SistemaEstoque:novo_item')

    if request.method == 'POST':
        form=NovoItemForm(request.POST)

        contexto={
            'form_action':form_action,
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('SistemaEstoque:home')
        
        return render(request, 'SistemaEstoque/novo_item.html', contexto)
    
    contexto={
            'form': NovoItemForm(),
            'form_action':form_action,}
    
    return render(request,'SistemaEstoque/novo_item.html', contexto)