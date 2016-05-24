from django.contrib import admin

from articles.models import Article, CommonUser


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'create_user', 'create_date')
    search_fields = ('title', 'create_user', 'create_date')

    class Meta:
        model = Article


class CommonUserAdmin(admin.ModelAdmin):
    list_display = ('username', )


admin.site.register(Article, ArticleAdmin)
admin.site.register(CommonUser, CommonUserAdmin)
