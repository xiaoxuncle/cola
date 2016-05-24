from django.contrib.auth.models import User
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=4000)
    create_user = models.ForeignKey(User)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        ordering = ("-create_date",)

    def __str__(self):
        return self.title

    def get_tags(self):
        return Tag.objects.filter(article=self)

    def create_tags(self, tags):
        tags = tags.strip()
        tag_list = tags.split(' ')
        for tag in tag_list:
            if tag:
                Tag.objects.get_or_create(tag=tag.lower(), article=self, )


class Tag(models.Model):
    tag = models.CharField(max_length=50)
    article = models.ForeignKey(Article)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.tag


class ArticleComment(models.Model):
    article = models.ForeignKey(Article)
    comment = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)

    class Meta:
        verbose_name = 'Article Comment'
        verbose_name_plural = 'Article Comments'

    def __str__(self):
        return '{user}-{article}'.format(user=self.user.username, article=self.article.title)


class CommonUser(User):
    avatar = models.ImageField(upload_to='avatar', default='avatar/default_avatar.png')

    class Meta:
        verbose_name = 'Common User'
        verbose_name_plural = 'Common Users'

    def __str__(self):
        return self.username