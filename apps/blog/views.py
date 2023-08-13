from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.db.models import Q
from .models import *
from .forms import *
# Create your views here.

def blog(request):
    articles = Article.objects.filter(status='active')
    return render(request, 'blog/blogFrontpage.html', {'title': 'Blog', 'articles': articles})

def my_blog(request):
    current_user = request.user 
    articles = Article.objects.filter(author=current_user)
    return render(request, 'blog/blogFrontpage.html', {'title': 'Blog', 'articles': articles})

def details_blog(request, slug):
    article = get_object_or_404(Article, slug=slug, status='active')
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
            return  redirect('details_blog', slug=slug)
    else:
        form = CommentForm()
    
    return render(request, 'blog/details.html', {'article': article, 'form': form})

def search_blog(request):
    query = request.GET.get('query', '')
    articles = Article.objects.filter(Q(tags__icontains=query) |Q(category__icontains=query) |Q(title__icontains=query) | Q(content__icontains=query) | Q(content_preview__icontains=query), status='active')
    return render(request, 'blog/search.html', {'articles': articles, 'title': "Пошук по сайту", 'query': query})

def create_blog(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
               
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('details_blog', slug=article.slug)
    else:
        form = ArticleForm()
    return render(request, 'blog/create.html', {'form': form, 'title': "Створення статті"})

def update_blog(request, slug):
    article = get_object_or_404(Article, slug=slug, author=request.user)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        
        if form.is_valid():
            article = form.save()
            return redirect('details_blog', slug=article.slug)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'blog/update.html', {'form': form, 'title': "Оновлення статті"})

def delete_blog(request, slug):
    article = get_object_or_404(Article, slug=slug, author=request.user)
    article.delete()
    return redirect('blog')