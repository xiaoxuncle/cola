#!coding:utf-8
from django.contrib.auth.models import User
from django.db import models


class Node(models.Model):
    name = models.CharField(max_length=20, unique=True)
    create_user = models.ForeignKey(User)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def node_names(self):
        nodes = Node.objects.all()
        for node in nodes:
            yield node.name


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=4000)
    create_user = models.ForeignKey(User)
    create_date = models.DateTimeField(auto_now_add=True)
    node = models.ForeignKey(Node)

    class Meta:
        ordering = ("-create_date",)

    def __str__(self):
        return self.title

    def add_node(self, node_name):
        self.node = Node.objects.get(name=node_name)


class ArticleComment(models.Model):
    article = models.ForeignKey(Article)
    comment = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)

    def __str__(self):
        return '{user}-{article}'.format(user=self.user.username, article=self.article.title)

