from django.conf.urls import patterns, include, url
from .views import RenderHome

urlpatterns = [
	url(r'^$', RenderHome, name='home'),
]