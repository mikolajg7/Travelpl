from django.shortcuts import render, redirect
from django.forms.models import model_to_dict
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
    return render(request, 'login.html')
def registration_view(request):
    return render(request, 'registration.html')
