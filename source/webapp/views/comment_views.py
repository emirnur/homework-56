from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView, ListView

from webapp.forms import CommentForm, ArticleCommentForm
from webapp.models import Comment, Article


class CommentListView(ListView):
    template_name = 'comment/list.html'
    model = Comment
    context_object_name = 'comments'
    ordering = ['-created_at']
    paginate_by = 10
    paginate_orphans = 3


class CommentForArticleCreateView(CreateView):
    model = Comment
    template_name = 'comment/create.html'
    form_class = ArticleCommentForm

    def form_valid(self, form):
        article = get_object_or_404(Article, pk=self.kwargs.get('pk'))
        comment = article.comments.create(**form.cleaned_data)
        return redirect('article_view', pk=comment.article.pk)


class CommentCreateView(CreateView):
    model = Comment
    template_name = 'comment/create.html'
    form_class = CommentForm

    def get_success_url(self):
        return reverse('article_view', kwargs={'pk': self.object.article.pk})
