from django.conf.urls import patterns, include, url 
from django.contrib import admin


urlpatterns = patterns('',
    url(r'^userapp/', include('userapp.urls', namespace="userapp")),
    url(r'^admin/', include(admin.site.urls)),
)