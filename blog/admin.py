from django.contrib import admin
from .models import Post, Page, BlogTitle

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'text']
    list_display = ('title', 'published_date')
    list_filter = ['published_date']

    def save_model(self, request, obj, form, change): # So logged-in user is author by default
        obj.author = request.user
        obj.save()

class PageAdmin(admin.ModelAdmin):
    fields = ['title', 'text']

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()

class BlogTitleAdmin(admin.ModelAdmin):
    fields = ['text']
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True

admin.site.register(Post, PostAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(BlogTitle, BlogTitleAdmin)

admin.site.site_title = "Dropshadow Admin"
admin.site.site_header = "Dropshadow Admin"