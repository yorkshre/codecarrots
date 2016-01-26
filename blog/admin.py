from django.contrib import admin
from blog.models import Post
from blog.models import Bio
from blog.models import Patronage

admin.site.register(Post)
admin.site.register(Bio)
admin.site.register(Patronage)
