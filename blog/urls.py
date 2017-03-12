from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<entry_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<entry_id>[0-9]+)/new_comment$', views.new_comment, name='new_comment'),
]
