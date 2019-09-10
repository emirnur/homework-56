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

        errors = {}

        if not title:
            errors['title'] = 'Title should not be empty!'
        elif len(title) > 200:
            errors['title'] = 'Title should have length of 200 symbols or less!'

        if not author:
            errors['author'] = 'Author should not be empty!'
        elif len(author) > 40:
            errors['author'] = 'Author should have length of 40 symbols or less!'

        if not text:
            errors['text'] = 'Text should not be empty!'
        elif len(text) > 3000:
            errors['text'] = 'Text should have length of 3000 symbols or less!'

        if len(errors) > 0:
            article = Article(title=title, author=author, text=text)
            return render(request, 'create.html', context={'errors': errors, 'article': article})

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

        errors = {}

        if not article.title:
            errors['title'] = 'Title should not be empty!'
        elif len(article.title) > 200:
            errors['title'] = 'Title should have length of 200 symbols or less!'

        if not article.author:
            errors['author'] = 'Author should not be empty!'
        elif len(article.author) > 40:
            errors['author'] = 'Author should have length of 40 symbols or less!'

        if not article.text:
            errors['text'] = 'Text should not be empty!'
        elif len(article.text) > 3000:
            errors['text'] = 'Text should have length of 3000 symbols or less!'

        if len(errors) > 0:
            return render(request, 'update.html', context={'errors': errors, 'article': article})

        article.save()
        return redirect('article_view', pk=article.pk)


def article_delete_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', context={'article': article})
    elif request.method == 'POST':
        article.delete()
        return redirect('index')
