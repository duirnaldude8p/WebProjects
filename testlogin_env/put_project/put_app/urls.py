from django.conf.urls import url

urlpatterns[
	url(r'^$', views.Put_Data.as_view(), name="put_app"),
]