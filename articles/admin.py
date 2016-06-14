from django.contrib import admin
from authentication.models import CommonUser
from articles.models import Article, Node

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'create_user', 'create_date')
    search_fields = ('title', 'create_user', 'create_date')


@admin.register(Node)
class NodeAdmin(admin.ModelAdmin):
	list_display = ('name', )