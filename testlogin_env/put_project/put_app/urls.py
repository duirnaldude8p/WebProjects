from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.Put_Data.as_view(), name="put_app"),
]