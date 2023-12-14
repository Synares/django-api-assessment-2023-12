from django.contrib import admin

from .models import Post, Comment

# Register models here to access them in admin
admin.site.register(Post)
admin.site.register(Comment)
