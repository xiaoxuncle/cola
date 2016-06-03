#!coding:utf-8
from django import forms

from articles.models import Article


class ArticleForm(forms.Form):
    node_choices = [
        ('1', 'linux'),
        ('2', 'python'),
        ('3', 'v2ex'),
        ('4', 'iOS')
    ]

    title = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'请输入主题标题'}), max_length=255)
    content = forms.CharField(required=True, widget=forms.Textarea(attrs={'class':'form-control'}), max_length=4000)
    node = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}), choices=node_choices)
    tags = forms.CharField(required=False,
            widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Use spaces to separate the tags, such as "java jsf primefaces"'}),
            max_length=255)


