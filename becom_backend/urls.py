from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin


urlpatterns = [
	url(r'^', include('becom_web.urls')),
    url(r'^api/', include('RESTafari.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/', include('rest_framework_social_oauth2.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)