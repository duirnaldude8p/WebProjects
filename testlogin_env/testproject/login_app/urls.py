from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.Register_Data.as_view(), name='register'),
	url(r'^profile/$', views.profile_page, name='profile'),
    url(r'^login/$', views.Login_Data.as_view(), name='login'),
    # url(r'^regdata/$', views.GetRegData.as_view(), name='regdata'),
   
]