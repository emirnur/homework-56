from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView

from webapp.forms import CommentForm, ArticleCommentForm
from webapp.models import Comment, Article
from .base_views import ListView, CreateView


class CommentListView(ListView):
    template_name = 'comment/list.html'
    model = Comment
    context_key = 'comments'


class CommentForArticleCreateView(View):
    def post(self, request, *args, **kwargs):
        form = ArticleCommentForm(data=request.POST)
        article_pk = kwargs.get('pk')
        article = get_object_or_404(Article, pk=article_pk)
        if form.is_valid():
            comment = Comment.objects.create(
                author=form.cleaned_data['author'],
                text=form.cleaned_data['text'],
                article=article
            )
            return redirect('article_view', pk=article_pk)
        else:
            return render(request, 'article/article.html', context={'form': form, 'article': article})


class CommentCreateView(CreateView):
    model = Comment
    template_name = 'comment/create.html'
    form_class = CommentForm

    def get_redirect_url(self):
        return reverse('article_view', kwargs={'pk': self.object.article.pk})
