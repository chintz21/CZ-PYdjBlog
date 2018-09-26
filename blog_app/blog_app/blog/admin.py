from django.contrib import admin

# Register your models here.

from blog.models import BlogAuthor, Blog, BlogComment

admin.site.register(BlogAuthor)
admin.site.register(Blog)
admin.site.register(BlogComment)

