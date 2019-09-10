from django import forms
from django.forms import widgets


class ArticleForm(forms.Form):
    title = forms.CharField(max_length=200, label='Title', required=True)
    author = forms.CharField(max_length=40, label='Author', required=True)
    text = forms.CharField(max_length=3000, label='Text', required=True,
                           widget=widgets.Textarea)
