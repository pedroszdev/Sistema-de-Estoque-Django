from django.shortcuts import render

def inventario(request):
    return render(request,'SistemaEstoque/inventario.html')