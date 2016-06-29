from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
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
            article.create_user = request.user
            article.title = form.cleaned_data.get('title')
            article.content = form.cleaned_data.get('content').replace('\n', '<br>')
            node_name = form.cleaned_data.get('node')
            article.add_node(node_name)
            article.save()
            return index(request)
    else:
        form = ArticleForm()
        return render(request,'add_article.html', {'form': form})


def index(request):
    articles = Article.objects.order_by('-create_date')
    return render(request, 'index.html', {'articles': articles})


def article(request, article_id):
    article = Article.objects.get(id=article_id)
    comments = ArticleComment.objects.filter(article=article)
    return render(request, 'article.html', {'article': article, 'comments':comments})

@login_required(login_url='auth/signin')
def add_comment(request):
    if request.method == 'POST':
        content = request.POST.get('content').replace('\r', '<br>')
        id = request.POST.get('article_id')
        article = Article.objects.get(id=int(id))
        comment = ArticleComment(comment=content, user=request.user, article=article)
        comment.save()
        return redirect('/articles/' + id +'#' + id)
    else:
        return HttpResponseBadRequest()