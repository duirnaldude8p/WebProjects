from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.main_page, name='main_page'),
    url(r'^download_page/$', views.download_page, name='download_page'),
    url(r'^create_page/$', views.create_page, name='create_page'),
]
