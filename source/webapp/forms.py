from django import forms
from django.forms import widgets

from webapp.models import Category


class ArticleForm(forms.Form):
    title = forms.CharField(max_length=200, label='Title', required=True)
    author = forms.CharField(max_length=40, label='Author', required=True)
    text = forms.CharField(max_length=3000, label='Text', required=True,
                           widget=widgets.Textarea)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False, label='Category',
                                      empty_label=None)
