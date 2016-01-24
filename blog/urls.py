from django.conf.urls import include, url
import blog
import pprint
urlpatterns = [
    url(r'^$', blog.views.main.list),
    url(r'^post/(?P<pk>[0-9]+)/$', blog.views.main.detail),

    # pprint.pprint (blog.views.aboutus.list)
    #url(r'^onas$', views.onas.list)
 ]
