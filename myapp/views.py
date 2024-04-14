from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.forms.models import model_to_dict
from django.contrib import messages
from .utils import get_random_posts
from .forms import PostForm
from .models import Post
import requests

posts = get_random_posts()[:5]
def home(request):
    if 'new_post' in request.session:
        new_post_id = request.session['new_post']['id']
        new_post = Post.objects.get(id=new_post_id)
        posts.insert(0, model_to_dict(new_post))
        del request.session['new_post']
    return render(request, 'home.html', {'posts': posts})

def add_post(request):
    if request.method == 'POST':
        content = request.POST.get('body')
        new_post = Post.objects.create(body=content)
        request.session['new_post'] = model_to_dict(new_post)
        return redirect('home')


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        passw = request.POST['passw']

        user=authenticate(request, username=username, password = passw)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Błąd logowania. Sprawdź nazwę użytkownika i hasło.')
            return redirect('login')


    return render(request, 'login.html')




def registration_view(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1 != pass2:
            messages.error(request, 'Hasła nie są takie same.')
            return redirect('registration')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Użytkownik o podanej nazwie już istnieje.')
            return redirect('registration')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Adres email jest już używany.')
            return redirect('registration')
        
        if len(pass1) < 6:
            messages.error(request, 'Hasło musi mieć co najmniej 8 znaków.')
            return redirect('registration')
        
        myuser = User.objects.create_user(username, email, pass1)
        myuser.save()
        return redirect('login')
    
    return render(request, 'registration.html')

def logout_met(request):
    logout(request)
    messages.error(request, "Wylogowano")
    return redirect('login')
