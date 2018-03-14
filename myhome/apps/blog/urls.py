# -*- coding:utf-8 -*-
from django.conf.urls import url
from . import views
from django.views.generic import TemplateView


app_name = 'blog'
urlpatterns = [
    url(r'^$', views.INdexView.as_view(), name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetailView.as_view(), name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.ArchivesView.as_view(), name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name='category'),
    url(r'^tag/(?P<pk>[0-9]+)/$', views.TagView.as_view(), name='tag'),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^search/', views.search, name='search'),
]