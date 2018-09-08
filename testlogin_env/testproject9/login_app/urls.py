from . import views
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
	url(r'^$', views.login, name='login'),
	url(r'^register/$', views.register, name='register'),
	url(r'^profile/$', views.profile, name='profile'),
	url(r'^getprofiledata/$', views.GetProfileData.as_view(), name='getprofiledata'),
	url(r'^postprofiledata/$', views.PostProfileData.as_view(), name='postprofiledata'),
]


urlpatterns = format_suffix_patterns(urlpatterns)