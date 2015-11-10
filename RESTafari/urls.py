from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'becom_backend.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^beacon/', 'RESTafari.views.beacon', name='beacon'),

)
