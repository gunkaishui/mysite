from django.contrib import admin
from blog.models import *
# Register your models here.

admin.site.register(BlogUser)
admin.site.register(Article)
admin.site.register(ComTent)
admin.site.register(Like)
