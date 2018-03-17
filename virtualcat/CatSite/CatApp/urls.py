from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^$', views.main, name="main"),
    # url(r'^maindata/$', views.MainData.as_view(), name='maindata'),
    # url(r'^accountdata/$', views.AccountData.as_view(), name='accountdata'),
    url(r'^getcatdata/$', views.CatGetData.as_view(), name='getcatdata'),
    url(r'^postcatdata/$', views.CatPostData.as_view(), name='postcatdata'),
    # url(r'^getcatcommentdata/$', views.CatCommentGetData.as_view(), name='getcatcommentdata'),
    # url(r'^postcatcommentdata/$', views.CatCommentPostData.as_view(), name='postcatcommentdata'),
    # url(r'^getcomment/$', views.CommentGetData.as_view(), name='getcomment'),
   	# url(r'^postcomment/$', views.CommentPostData.as_view(), name='postcomment'),
   	url(r'^getuser/$', views.UserGetData.as_view(), name='getuser'),
   	url(r'^postuser/$', views.UserPostData.as_view(), name='postuser'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
