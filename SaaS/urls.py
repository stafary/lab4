from django.conf.urls import patterns, include, url
import settings
#from django.contrib import admin
from lib import views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SaaS.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$',views.home),
    url(r'^query_result/$',views.show_query_result),
    url(r'^details/$', views.show_details),
    url(r'^add/$',views.add_book),
    url(r'^add_author/$',views.add_author),
    url(r'^update/$',views.update),
    url(r'^success/$',views.success),
    url(r'^add_Author/$',views.add_Author),
    url( r'^static/(?P<path>.*)$', 'django.views.static.serve',
                                            { 'document_root':settings.STATIC_URL }),

#    url(r'^update/$', views.update)
)
