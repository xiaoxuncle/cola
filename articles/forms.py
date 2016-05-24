from django import forms

from articles.models import Article


class ArticleForm(forms.ModelForm):
    title = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}), max_length=255)
    content = forms.CharField(required=True, widget=forms.Textarea(attrs={'class':'form-control'}), max_length=4000)
    tags = forms.CharField(required=False,
            widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Use spaces to separate the tags, such as "java jsf primefaces"'}),
            max_length=255)


    class Meta:
        model = Article
        fields = ['title', 'content', 'tags']