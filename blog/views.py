from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404


# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    patrons = [
        { "src":"/static/img/fundacja_infolet.jpg"},
        { "src":"/static/img/osworld.jpg"},
    ]
    partners = [
        { "src":"/static/img/infolet.jpg"},
        { "src":"/static/img/osworld.jpg"},
    ]
    sponsors = [
        { "src":"/static/img/indeks.jpeg"},
    ]
    size_patrons = 12/len(patrons)
    size_partners = 12/len(partners)
    size_sponsors = 12/len(sponsors)
    return render(request, 'blog/post_list.html', {
        'posts':posts,
        'patrons':patrons,
        'partners':partners,
        'sponsors':sponsors,
        'size_partners':size_partners,
        'size_patrons':size_patrons,
        'size_sponsors':size_sponsors,
        })
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
