from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
def login_view(request):
    return render(request, 'login.html')
def registration_view(request):
    return render(request, 'registration.html')
