# -*- coding:utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse ,HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import login,logout,authenticate
from django.core.urlresolvers import reverse
from  blog.forms import *
from blog.models import *
from django.views import generic
# Create your views here.

def index(request):
    form = LoginForm()
    return render(request,'blog/index.html',{'form':form})

def log_in(request):
    if request.method == 'GET':
       form = LoginForm()
       return render(request,'blog/index.html',{'form':form})
    else:
       form = LoginForm(request.POST)
       if form.is_valid():
            username = form.cleaned_data['uid']
            password = form.cleaned_data['pwd']
            user = authenticate(username=username,password=password)
            if user  and user.is_active:
               login(request,user)
               return redirect(reverse('blog:afterlogin'))
            else:
               msg = 'username or password is not true!'
               return render(request,'blog/index.html',{'form':form,'msg':msg})
       else:
             msg = 'the format is not correct!'
             return render(request,'blog/index.html',{'form':form,'msg':msg})

def register(request):
    if request.method == 'GET':
       form = RegisterForm()
       return render(request,'blog/register.html',{'form':form})
    else:
       form = RegisterForm(request.POST)
       if form.is_valid():
          username = form.cleaned_data['username']
          password1 = form.cleaned_data['password1']
          password2 = form.cleaned_data['password2']
          try:
             user = BlogUser.objects.get(username=username)
          except ObjectDoesNotExist: 
             if password1 != password2:
                msg = 'two password is not same!'
                return render(request,'blog/register.html',{'form':form,'msg':msg})      
             else:
                 newuser = BlogUser()
                 newuser.username = username
                 newuser.set_password(password1)
                 newuser.save()
                 return redirect(reverse('blog:login'))
          else:
              msg = 'the username is already exist!'
              return render(request,'blog/register.html',{'form':form,'msg':msg})
       else:      
           msg = 'format is not correct!'
           return render(request,'blog/register.html',{'form':form,'msg':msg})

#@login_required 
"""class IndexView(generic.ListView):
     template_name = 'blog/after_login.html'
     context_object_name = 'article_list'
     def get_queryset(self):
         return Article.objects.order_by('-pub_date')[0:10]"""
@login_required
def index_view(request):
    articles = Article.objects.order_by('-pub_date')[0:10]
    return render(request,'blog/after_login.html',{'article_list':articles})

#@login_required
"""class DetailView(generic.DetailView):
      template_name = 'blog/detail.html'
      model = Article"""
@login_required
def detail(request,pk):
     article = get_object_or_404(Article,pk=pk)
     return render(request,'blog/detail.html',{'article':article})

@login_required
def comment(request,pk):
    newcomment = ComTent()
    newcomment.article = get_object_or_404(Article,pk=pk)
    newcomment.user = request.user
    newcomment.com_date =timezone.now()
    newcomment.content = request.POST['comtext']
    newcomment.save()
    newcomment.article.comments =newcomment.article.comments + 1 
    newcomment.article.save()
    return render(request,'blog/detail.html',{'article':newcomment.article})
      

@login_required
def log_out(request):
    logout(request)
    return redirect(reverse('blog:index'))
    
    
@login_required
def like(request,pk):
    article = get_object_or_404(Article,pk=pk)
    user = request.user
    try:
        Like.objects.get(article=article,user=user)
    except ObjectDoesNotExist:
        article.likes =article.likes + 1
        article.save()
        new_like = Like()
        new_like.article = article
        new_like.user = request.user
        new_like.save()
    return HttpResponseRedirect(reverse('blog:detail',args=(article.id,)))
@login_required
def mycomment(request):
       comments = request.user.comtent_set.order_by('-com_date')
       return render(request,'blog/mycomment.html',{'comment_list':comments})
@login_required
def keep(request,pk):
    article = get_object_or_404(Article,pk=pk)
    user = request.user
    try:
        keeped = Keep.objects.get(article=article,user=user)
    except ObjectDoesNotExist:
        newkeep = Keep()
        newkeep.article = article
        newkeep.user = user
        article.keeps = article.keeps + 1
        article.save()
        newkeep.save()
    return HttpResponseRedirect(reverse('blog:detail',args=(article.id,)))
   

def mykeep(request):
    keep_list = request.user.keep_set.order_by('-keep_date')
    return render(request,'blog/keep.html',{'keep_list':keep_list})
