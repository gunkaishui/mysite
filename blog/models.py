# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class BlogUser(AbstractUser):
    profile =models.CharField('profile',default='',max_length=256)
    def __unicode__(self):
        return self.username

class Article(models.Model):
    author = models.ForeignKey(BlogUser)
    title = models.CharField(max_length=256)
    content = models.TextField('content')
    pub_date = models.DateTimeField(auto_now_add=True,editable=True)
    likes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    keeps = models.IntegerField(default=0)
#    user = models.ManyToManyField(BlogUser,blank=True)
    
    def __unicode__(self):
        return self.title 
  
    class Meta:
        verbose_name = 'article'
        verbose_name_plural = 'article'

class ComTent(models.Model): #评论（注意：是评论的内容，非评论的数目！)
      article = models.ForeignKey(Article)
      user = models .ForeignKey(BlogUser)
      content = models.CharField(max_length=256)
      com_date = models.DateTimeField(auto_now=True,null=True)
      def __unicode__(self):
         return self.content
class Like(models.Model):
      article = models.ForeignKey(Article)
      user = models.ForeignKey(BlogUser)
      def __unicode__(self):
          return self.article.title

class Keep(models.Model):
      user = models.ForeignKey(BlogUser)
      article = models.ForeignKey(Article)
      keep_date = models.DateTimeField(auto_now=True,null=True)
      def __unicode__(self):
          return self.article
