from django.shortcuts import render, redirect
from .forms import *
from django.http import Http404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate, login, logout, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

def view_login(request):

    if request.POST:
        form_data = request.POST
        form = AcessForm(form_data)
    else:
        form = AcessForm()

    return render(request, 'pages/login.html', {'form': form})

def view_acess_login(request):
    if (not request.POST):
        raise Http404()
    
    post = request.POST

    form = AcessForm(post)

    if form.is_valid():
        usern = post['username']
        passwd = post['password']

        user = User.objects.filter(username = usern)

        if user:
            check_p = check_password(passwd, user[0].password)
            authenticated_user = authenticate(username = usern, password = passwd)
            if check_p:
                messages.success(request, 'Login realizado com sucesso!')
                login(request, authenticated_user)

                if 'login_count' in request.session:
                    request.session['login_count'] += 1
                else:
                    request.session['login_count'] = 1
                
                return redirect('usuarios:area_usuario')
            else:
                messages.error(request, 'Login ou senha incorretos.')
        else:
            messages.error(request, 'Login ou senha incorretos.')
    else:
        messages.error(request, 'Dados inválidos.')
    
    return redirect('usuarios:login')

##def view_logout(request):


def view_cadusuario(request, firstacess=0):

    if firstacess == 1:
        register_form = request.session.get("register_form", None)
        form = RegisterForm(register_form)
    else:
        if request.session.get("register_form"):
            del(request.session["register_form"])
        form = RegisterForm() 
    
    return render(request, 'pages/cadusuario.html', {'form': form})

def view_create_usuario(request):
    if not request.POST:
        raise Http404()
    
    
    post = request.POST
    request.session["register_form"] = post

    form = RegisterForm(post)

    if form.is_valid():
        form.save()
        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()
        messages.success(request, "Usuário cadastrado com sucesso!")
        del(request.session["register_form"])

    return redirect('usuarios:cadastro', firstacess = 1)

@login_required(login_url='usuarios:login', redirect_field_name ='next')
def view_area_usuario(request):
    login_count = request.session.get('login_count')
    return render(request, 'pages/areausuario.html', {'login_count': login_count})

@login_required(login_url='usuarios:login', redirect_field_name ='next')
def view_logout(request):
    if not request.POST:
        redirect('usuarios:login')

    logout(request)

    return redirect('usuarios:login')