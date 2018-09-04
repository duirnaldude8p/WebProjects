from . import views
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
	url(r'^$', views.pencilcases, name='pencilcases'),
	url(r'^postpencilcase/$', views.casecreator, name='postpencilcase'),
	url(r'^getcasedata/$', views.GetPencilCaseData.as_view(), name='getcasedata'),
	url(r'^postcasedata/$', views.PostPencilCaseData.as_view(), name='postcasedata'),
	# url(r'^putcasedata/(?P<pk>[0-9]+)/(?P<field>[\w\-]+)/$', views.PutPencilCaseData.as_view(), name='putcasedata'),
	url(r'^putcasedata/(?P<pk>[0-9]+)$', views.PutPencilCaseData.as_view(), name='putcasedata'),
	# url(r'^putcasedata/(?P<pk>[0-9]+)/(?P<rubber>[\w\-]+)/$', views.PutPencilCaseData.as_view(), name='putcasedata'),
	# url(r'^putcasedata/(?P<pk>[0-9]+)/(?P<pen>[\w\-]+)/$', views.PutPencilCaseData.as_view(), name='putcasedata'),
]


urlpatterns = format_suffix_patterns(urlpatterns)