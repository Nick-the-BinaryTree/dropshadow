from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Page

PAGES = Page.objects.all()

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts, 'pages': PAGES})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post, 'pages': PAGES})

def page(request, pg):
    page = get_object_or_404(Page, title=pg)
    return render(request, 'blog/page.html', {'page': page, 'pages': PAGES})

def handler404(request):
    response = render(request, 'blog/404.html', {'pages': PAGES})
    response.status_code = 404
    return response