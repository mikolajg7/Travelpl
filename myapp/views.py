from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.forms.models import model_to_dict
from django.contrib import messages
from django.conf import settings
from .utils import get_random_posts
from .forms import PostForm
from .models import Post
import requests
from django.contrib.auth import update_session_auth_hash
from django.core.mail import send_mail

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
        
        emaillist = [email]
        myuser = User.objects.create_user(username, email, pass1)
        myuser.save()
        send_mail('Witaj!',"Dziękujemy ci za zarejestrowanie sie na naszej aplikacji Travelpl!",'settings.EMAIL_HOST_USER',emaillist,fail_silently=False)
        return redirect('login')
    
    return render(request, 'registration.html')


def accountOptions_met(request):
    
    if request.method == 'POST':
        user = request.user
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1 != pass2:
            messages.error(request, 'Hasła nie są takie same.')
            return redirect('accountOptions')
        
        if username and username != user.username:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Użytkownik o podanej nazwie już istnieje.')
                return redirect('accountOptions')

        if email and email != user.email:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Adres email jest już używany.')
                return redirect('accountOptions')
        
        if pass1:
            if len(pass1) < 8:
                messages.error(request, 'Hasło musi mieć co najmniej 8 znaków.')
                return redirect('accountOptions')
        
            
        user.username = username
        user.email = email
        user.set_password(pass1)
        update_session_auth_hash(request, user)
        user.save()
        messages.success(request, 'Twoje dane zostały zaktualizowane.')
        return redirect('accountOptions')

    return render(request, 'accountOptions.html')


def logout_met(request):
    logout(request)
    messages.error(request, "Wylogowano")
    return redirect('login')

def accountOptions(request):
    user = User.objects.get(pk=request.user.pk) 
    return render(request, 'accountOptions.html', {'user': user})
