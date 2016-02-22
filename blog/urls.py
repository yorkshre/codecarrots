from django.conf.urls import include, url
import blog

urlpatterns = [
    url(r'^$', blog.views.main.list),
    url(r'^post/(?P<pk>[0-9]+)/$', blog.views.main.detail),

    url(r'^onas/(?P<pk>[0-9]+)/$', blog.views.aboutus.detail),
    url(r'^onas/ajax/(?P<pk>[0-9]+)/$', blog.views.aboutus.ajax),
    url(r'^onas$', blog.views.aboutus.list),

    url(r'^kontakt$', blog.views.contact.main)
 ]
