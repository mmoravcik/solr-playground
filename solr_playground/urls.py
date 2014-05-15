from django.conf.urls import patterns, include, url

from haystack import urls as haystack_urls
from django.contrib import admin
from apps.search.views import HomeView
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'solr_playground.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^search/', include(haystack_urls)),
    url(r'^admin/', include(admin.site.urls)),
    url('', HomeView.as_view()),
)
