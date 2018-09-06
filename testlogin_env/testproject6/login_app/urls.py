from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
	url(r'^$', views.userlogin, name='login'),
	url(r'^register/$', views.userregister, name='register'),
	url(r'^profile/$', views.userprofile, name='profile'),
	url(r'^postprofiledata/$', views.PostProfileData.as_view(), name='postprofiledata'),
	url(r'^getprofiledata/$', views.GetProfileData.as_view(), name='getprofiledata'),
]

urlpatterns = format_suffix_patterns(urlpatterns)