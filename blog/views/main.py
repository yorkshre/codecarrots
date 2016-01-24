from django.shortcuts import render
from django.utils import timezone
from blog.models import Post
from blog.models import Patronage
from blog.models import Menu
from django.shortcuts import render, get_object_or_404


# Create your views here.
def list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/posts/list.html', {
    'patronage':Patronage.list,
    'menu':Menu.options(),
    'posts':posts
    })

def detail(request, pk):
        post = get_object_or_404(Post, pk=pk)
        return render(request, 'blog/posts/detail.html', {
        'patronage':Patronage.list,
        'menu':Menu.options(),
        'post': post
        })
