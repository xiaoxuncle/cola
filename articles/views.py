from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect, render
from django.template import RequestContext

from articles.forms import ArticleForm
from articles.models import Article, ArticleComment
from authentication.models import CommonUser

@login_required(login_url='/auth/signin')
def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = Article()
            article.create_user = CommonUser.objects.get(user=request.user)
            article.title = form.cleaned_data.get('title')
            article.content = form.cleaned_data.get('content')
            article.save()
            tags = form.cleaned_data.get('tags')
            article.create_tags(tags)
            return index(request)
    else:
        form = ArticleForm()
        return render_to_response('add_article.html', {'form': form}, context_instance=RequestContext(request))


def index(request):
    articles = Article.objects.order_by('-create_date')
    return render_to_response('index.html', {'articles': articles}, context_instance=RequestContext(request))


def article(request, article_id):
    article = Article.objects.get(id=article_id)
    tags = Article().get_tags()
    return render_to_response('article.html', {'article': article, 'tags': tags}, context_instance=RequestContext(request))


def add_comment(request):
    content = request.POST.get('content', '')
    id = request.POST.get('article_id', '')
    user = CommonUser.objects.get(user=request.user)
    article = Article.objects.get(id=id)
    comment = ArticleComment(comment=content, user=user, article=article)
    comment.save()