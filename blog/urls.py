from django.conf.urls import url
from blog.views import *
urlpatterns = [
    url(r'^$',index,name='index'),
    url(r'^mycomment/$',mycomment,name='mycomment'),
    url(r'^mykeep/$',mykeep,name='mykeep'),
    url(r'^login/',log_in,name='login'),
    url(r'^register/',register,name='register'),
    url(r'^(?P<pk>[0-9]+)/$',detail,name='detail'),
    url(r'^(?P<pk>[0-9]+)/comment/$',comment,name='comment'),
    url(r'^(?P<pk>[0-9]+)/like/$',like,name='like'),
    url(r'^(?P<pk>[0-9]+)/keep/$',keep,name='keep'),
    url(r'^firstpage/$',index_view,name='afterlogin'),
    url(r'^logout/$',log_out,name='logout'),
    ]
