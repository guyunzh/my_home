from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^login/$', views.user_login, name='user_login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^changepwd/$', views.change_pwd, name='changepwd'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'blog/account/logout.html'}, name='logout'),
]