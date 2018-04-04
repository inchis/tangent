from rest_framework.authtoken import views
from django.conf.urls.defaults import *
from django.views.generic import TemplateView
from django.contrib import admin
from tang.views import UserList
from rest_framework.urlpatterns import format_suffix_patterns
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', UserList.as_view()),
                       url(r'^api-token-auth/', views.obtain_auth_token),
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       #url(r'^$', 'tang.views.UserList', name="dashboard"),
                       url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                       )

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])