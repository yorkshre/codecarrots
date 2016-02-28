from blog.models import Menu
from django.shortcuts import render
from django.template import RequestContext
from blog.models import Patronage
from blog.models import Links


def list(request):
    return render(request, 'blog/files/list.html', {
        'context_instance': RequestContext(request),
        'menu': Menu.options(),
        'patronage': Patronage.list,
        'links': Links.all()
    })
