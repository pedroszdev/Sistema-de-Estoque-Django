from django.shortcuts import render, redirect
from SistemaEstoque.forms import  RegisterForm, RegisterUpdateForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

def criar_user(request):
    form = RegisterForm()
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('SistemaEstoque:home')
    
    contexto={
        'form': form
    }


    return render(request, 'SistemaEstoque/criar_usuario.html', contexto)

def atualizar_user(request):

    form = RegisterUpdateForm(instance=request.user)
    
    if request.method == 'POST':
        form = RegisterUpdateForm(data=request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('SistemaEstoque:home')
    
    contexto={
        'form': form
    }



    return render(request, 'SistemaEstoque/criar_usuario.html', contexto)

def login_user(request):

    form= AuthenticationForm(request)
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect('SistemaEstoque:home')

    contexto={
        'form': form
    }

    return render(request, 'SistemaEstoque/login.html', contexto)

def logout(request):
    auth.logout(request)
    return redirect('SistemaEstoque:login')