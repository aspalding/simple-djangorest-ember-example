from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^todos/', include('todos.urls', namespace="todos")),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
