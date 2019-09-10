from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Article


def index_view(request, *args, **kwargs):
    articles = Article.objects.all()
    return render(request, 'index.html', context={
        'articles': articles
    })


def article_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'article.html', context={
        'article': article
    })


def article_create_view(request, *args, **kwargs):
    if request.method == 'GET':
        return render(request, 'create.html')
    elif request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        text = request.POST.get('text')
        article = Article.objects.create(title=title, author=author, text=text)
        return redirect('article_view', pk=article.pk)


def article_update_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'GET':
        return render(request, 'update.html', context={'article': article})
    elif request.method == 'POST':
        article.title = request.POST.get('title')
        article.author = request.POST.get('author')
        article.text = request.POST.get('text')
        article.save()
        return redirect('article_view', pk=article.pk)
