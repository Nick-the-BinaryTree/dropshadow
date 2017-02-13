from django.contrib import admin
from .models import Post, Page

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'text']
    list_display = ('title', 'published_date')
    list_filter = ['published_date']

class PageAdmin(admin.ModelAdmin):
    fields = ['title', 'text']

admin.site.register(Post, PostAdmin)
admin.site.register(Page, PageAdmin)

admin.site.site_title = "Dropshadow Admin"
admin.site.site_header = "Dropshadow Admin"