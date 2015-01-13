from django.conf.urls import patterns, url

from userapp import views

urlpatterns = patterns('',
	#ex: userapp
    url(r'^$', views.index, name='index'),
    #ex: userapp/detail
    url(r'^(?P<id>\d+)/$', views.detail, name='detail'),
   	#ex: userapp/update
    url(r'^update/(?P<id>\d+)/$', views.update, name='update'),
    #ex: userapp/delete
    url(r'^delete/(?P<id>\d+)/$', views.delete, name='delete'),

)