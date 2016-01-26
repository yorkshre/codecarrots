from blog.models import Menu
from blog.models import Patronage
from blog.models import Bio
from django.core import serializers
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse;

# Create your views here.
def list(request):
    return render(request, 'blog/bio/list.html', {
        'menu':Menu.options(),
        'bio': Bio.objects.all(),
        'patronage':Patronage.list
    })


def detail(request, pk):
        bio = get_object_or_404(Bio, pk=pk)
        return render(request, 'blog/bio/detail.html', {
            'bio': bio,
            'menu':Menu.options()
        })


def ajax(request, pk):
        bio = get_object_or_404(Bio, pk=pk)
        return JsonResponse({
            'bio': {
                'name': bio.name,
                'img': bio.img.url,
                'text': bio.text
            }
        })
