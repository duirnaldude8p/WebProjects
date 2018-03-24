from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^$', views.main, name="main"),
    url(r'^account/$', views.account, name='account'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='login'),
    url(r'^catlist/$', views.catlist, name='catlist'),
    url(r'^catpage/$', views.catpage, name='catpage'),
    url(r'^getmaindata/$', views.MainGetData.as_view(), name='getmaindata'),
    url(r'^postmaindata/$', views.MainPostData.as_view(), name='postmaindata'),
    url(r'^getaccountdata/$', views.AccountGetData.as_view(), name='getaccountdata'),
    url(r'^postaccountdata/$', views.AccountPostData.as_view(), name='postaccountdata'),
    url(r'^getcatdata/$', views.CatGetData.as_view(), name='getcatdata'),
    url(r'^postcatdata/$', views.CatPostData.as_view(), name='postcatdata'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
