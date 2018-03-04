from django.conf.urls import url
from .views import home, contact

app_name = 'main_app'
urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^contact/$', contact, name='contact'),
]