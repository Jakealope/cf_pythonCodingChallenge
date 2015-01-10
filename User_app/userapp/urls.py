from django.conf.urls import patterns, url

from userapp import views

urlpatterns = patterns('',
	#ex: userapp
    url(r'^$', views.index, name='index'),
    #ex: userapp/detail
    url(r'^(?P<user_id>\d+)/$', views.detail, name='detail'),
   
)