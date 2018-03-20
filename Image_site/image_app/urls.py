from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
	url(r'^$', views.main, name="main"),
    url(r'^getpicture/$', views.PictureGetData.as_view(), name='getpicture'),
    url(r'^postpicture/$', views.PicturePostData.as_view(), name='postpicture'),
]

urlpatterns = format_suffix_patterns(urlpatterns)