from django import forms
from django.core.exceptions import ValidationError

from webapp.models import Article, Comment, STATUS_ACTIVE


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ['created_at', 'updated_at', 'status']

    def clean_title(self):
        title = self.cleaned_data['title']
        min_length = 10
        if len(title) < min_length:
            raise ValidationError(
                'Title should be at least %(length)s symbols long.',
                code='title_too_short',
                params={'length': min_length}
            )
        return title.capitalize()

    def clean(self):
        super().clean()
        title = self.cleaned_data.get('title', '')
        text = self.cleaned_data.get('text', '')
        if title.lower() == text.lower():
            raise ValidationError('Text should not duplicate title')
        return self.cleaned_data


class CommentForm(forms.ModelForm):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.fields['article'].queryset = Article.objects.filter(status=STATUS_ACTIVE)

    # article = forms.ModelChoiceField(queryset=Article.objects.filter(status=STATUS_ACTIVE), label='Статья')

    class Meta:
        model = Comment
        exclude = ['created_at', 'updated_at']


class ArticleCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'text']


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Найти')
