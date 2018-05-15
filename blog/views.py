from django.shortcuts import render, redirect, reverse
from django.http.response import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.forms.formsets import formset_factory


from .forms import RegisterForm, LoginForm, ArticleForm, TagForm, BaseTagFormSet
from .models import Article, Tag

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


@login_required()
def add_article(request):
    #TODO СМОТРИ MESSAGE FRAMEWORK
    success = False
    user = request.user
    TagFormSet = formset_factory(TagForm, formset=BaseTagFormSet)
    article_form = ArticleForm()
    tag_formset = TagFormSet()
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        tag_formset = TagFormSet(request.POST)
        print(form.errors)
        if form.is_valid() and tag_formset.is_valid():
            print(user)
            f = form.save()
            f.owner = user
            for tag_form in tag_formset:
                tag = tag_form.cleaned_data.get('name')
                if tag is not None:
                    f.tags.add(Tag.objects.get(name=tag).id)
                    f.save()
            
                
            return redirect(reverse('index'))
        
    return render(request, 'blog/add_article.html', {'article_form': article_form, 'tag_formset': tag_formset, 'success': success})


def search_tag(request, tag_name):
    tag = Tag.objects.get(name=tag_name)
    articles = Article.objects.filter(tags=tag)
    return render(request, 'blog/tag_search.html', {'tag_name': tag_name, 'articles': articles})


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