from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework import routers

from todos import views


urlpatterns = patterns('',
    url(r'^$', views.Todos.as_view()),
    url(r'^(?P<pk>\d+)/$', views.Todo.as_view()),
)
