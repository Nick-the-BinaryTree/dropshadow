from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Page, BlogTitle

PAGES = Page.objects.all()
TITLE = BlogTitle.objects.all()
if TITLE:
    TITLE = TITLE[0]
else:
    TITLE = BlogTitle()

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts, 'pages': PAGES, 'title': TITLE})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post, 'pages': PAGES, 'title': TITLE})

def page(request, pg):
    page = get_object_or_404(Page, title=pg)
    return render(request, 'blog/page.html', {'page': page, 'pages': PAGES, 'title': TITLE})

def handler404(request):
    response = render(request, 'blog/404.html', {'pages': PAGES, 'title': TITLE})
    response.status_code = 404
    return response