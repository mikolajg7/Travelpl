from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    return render(request, 'home.html', {'user': request.user})


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
