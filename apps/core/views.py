from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Games
from .forms import *
# Create your views here.

def shop(request):
    products = Games.objects.all()
    return render(request, 'core/shopFrontpage.html', {'title': 'Shop', 'products': products})

def details(request, slug):
    product = get_object_or_404(Games, slug=slug)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = product
            comment.save()
            return  redirect('details', slug=slug)
    else:
        form = CommentForm()
    
    return render(request, 'core/details.html', {'product': product, 'form': form})

def search(request):
    query = request.GET.get('query', '')
    products = Games.objects.filter(Q(name_item__icontains=query) | Q(heros__name__icontains=query) | Q(raritys__name__icontains=query) | Q(cells__name__icontains=query))
    return render(request, 'core/search.html', {'products': products, 'query': query})

def create(request):
    if request.method == 'POST':
        form = GamesForm(request.POST, request.FILES)
               
        if form.is_valid():
            product = form.save(commit=False)
            product.author = request.user
            product.save()
            return redirect('shop')
    else:
        form = GamesForm()
    form.fields.pop('tags_input')
    return render(request, 'core/create.html', {'form': form, 'title': 'Створення товару'})

def update(request, slug):
    product = get_object_or_404(Games, slug=slug, author=request.user)
    if request.method == 'POST':
        form = GamesForm(request.POST, request.FILES, instance=product)
        
        if form.is_valid():
            product = form.save()
            return redirect('shop')
    else:
        form = GamesForm(instance=product)
    form.fields.pop('tags_input')
    return render(request, 'core/update.html', {'form': form, 'title': "Оновлення статті"})

def delete(request, slug):
    product = get_object_or_404(Games, slug=slug, author=request.user)
    product.delete()
    return redirect('shop')
