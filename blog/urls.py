from django.conf.urls import include, url
import blog
import pprint
urlpatterns = [
    url(r'^$', blog.views.main.list),
    url(r'^post/(?P<pk>[0-9]+)/$', blog.views.main.detail),

    url(r'^onas/(?P<pk>[0-9]+)/$', blog.views.aboutus.detail),
    url(r'^onas/ajax/(?P<pk>[0-9]+)/$', blog.views.aboutus.ajax),
    url(r'^onas$', blog.views.aboutus.list)
 ]
