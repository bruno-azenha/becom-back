from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin


urlpatterns = [
	url(r'^', include('becom_web.urls')),
    url(r'^api/', include('RESTafari.urls')),

    url(r'^admin/', include(admin.site.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)