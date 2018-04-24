from django.shortcuts import render, redirect, reverse
from django.http.response import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import RegisterForm, LoginForm
from .models import Article

# Create your views here.

def index(request):
    articles_list = Article.objects.all().order_by('-date')
    paginator = Paginator(articles_list, 7)
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    return render(request, 'blog/index.html', {'articles': articles})


def article(request, number):
    article = Article.objects.get(id=number)
    return render(request, 'blog/article.html', {'article': article})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        print(form.error_messages)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect(reverse('index'))
    else:
        form = RegisterForm()
    return render(request, 'blog/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            clean_data = form.cleaned_data
            user = authenticate(username=clean_data['username'],
                                password=clean_data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(reverse('index'))
                else:
                    return HttpResponse('Ошибка авторизации')
            else:
                return HttpResponse('Ошибка авторизации')
        return render(request, 'blog/index.html')
    
    
def logout_view(request):
    logout(request)
    return redirect(reverse('index'))