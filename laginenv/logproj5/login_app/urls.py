from . import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
	path('', views.login, name='login'),
	path('register/', views.register, name='register'),
	path('profile/', views.profile, name='profile'),
	path('getprofiledata/', views.GetProfileData.as_view(), name='getprofiledata'),
	path('postprofiledata/', views.PostProfileData.as_view(), name='postprofiledata'),
]


urlpatterns = format_suffix_patterns(urlpatterns)