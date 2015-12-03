from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = [
	url(r'^', include('becom_web.urls')),
    url(r'^api/', include('RESTafari.urls')),

    url(r'^admin/', include(admin.site.urls)),
]