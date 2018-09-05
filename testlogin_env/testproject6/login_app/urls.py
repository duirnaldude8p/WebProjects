from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
	url(r'^$', views.userlogin, name='login'),
	url(r'^register/$', views.userregister, name='register'),
	url(r'^profile/$', views.userprofile, name='profile'),
]

urlpatterns = format_suffix_patterns(urlpatterns)