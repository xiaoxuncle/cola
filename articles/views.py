from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect

from articles.forms import ArticleForm
from articles.models import Article


def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = Article()
            article.create_user = request.user
            article.title = form.cleaned_data.get('title')
            article.content = form.cleaned_data.get('content')
            article.save()
            tags = form.cleaned_data.get('tags')
            article.create_tags(tags)
            return index(request)
    else:
        form = ArticleForm()
    return render_to_response('add_article.html', {'form': form})


def login(request):
    return render_to_response('login.html')


def index(request):
    articles = Article.objects.order_by('-create_date')
    user = request.user
    return render_to_response('index.html', {'articles': articles})


def article(request, article_id):
    article = Article.objects.get(id=article_id)
    tags = Article().get_tags()
    return render_to_response('article.html', {'article': article, 'tags': tags})