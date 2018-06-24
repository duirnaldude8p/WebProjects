from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^$', views.main, name="home"),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^register/$', views.register, name='register'),
    url(r'^user_login/$', views.my_user_login, name='user_login'),
    url(r'^bigcatlist/$', views.bigcatlist, name='bigcatlist'),
    url(r'^bigcat/$', views.bigcat, name='bigcat'),
    url(r'^getmaindata/$', views.MainGetData.as_view(), name='getmaindata'),
    url(r'^postmaindata/$', views.MainPostData.as_view(), name='postmaindata'),
    url(r'^getprofiledata/$', views.ProfileGetData.as_view(), name='getprofiledata'),
    url(r'^postprofiledata/$', views.ProfilePostData.as_view(), name='postprofiledata'),
    # url(r'^getlogindata/$', views.CurrentAccountGetData.as_view(), name='getlogindata'),
    # url(r'^postlogindata/$', views.CurrentAccountPostData.as_view(), name='postlogindata'),
    # url(r'^getbigcatdata/$', views.BigCatGetData.as_view(), name='getbigcatdata'),
    # url(r'^postbigcatdata/$', views.BigCatPostData.as_view(), name='postbigcatdata'),
    # url(r'^getcommentdata/$', views.BigCommentData.as_view(), name='getcommentdata'),
    # url(r'^postcommentdata/$', views.BigCommentData.as_view(), name='postcommentdata'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
