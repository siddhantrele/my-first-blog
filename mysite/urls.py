from django.conf.urls import include, url
from django.contrib import admin
import django.contrib.auth.views
admin.autodiscover()

urlpatterns = [
    url(r'^jet/', include('jet.urls', 'jet')),
	url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')), 
    url(r'^admin/', include(admin.site.urls)),
	url(r'^accounts/login/$', django.contrib.auth.views.login),
	url(r'^accounts/logout/$', django.contrib.auth.views.logout, {'next_page': '/'}),
    url(r'', include('blog.urls')),
]