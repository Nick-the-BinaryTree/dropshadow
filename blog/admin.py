from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'text']
    list_display = ('title', 'published_date')

admin.site.register(Post, PostAdmin)

