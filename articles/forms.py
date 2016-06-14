#!coding:utf-8
from django import forms

from articles.models import Article, Node


class ArticleForm(forms.Form):
    node_choices = []
    node_names = Node().node_names()
    for name in list(node_names):
    	node_choices.append((name, name))
    title = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'请输入主题标题'}), max_length=255)
    content = forms.CharField(required=True, widget=forms.Textarea(attrs={'class':'form-control'}), max_length=4000)
    node = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}), choices=node_choices)

