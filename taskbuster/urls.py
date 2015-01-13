from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import home, home_files

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'taskbuster.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^(?P<filename>(robots.txt)|(humans.txt))$', home_files, name='home-files'), 
    url(r'^admin/', include(admin.site.urls)),
)
