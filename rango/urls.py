from django.conf.urls import patterns, url
from django.contrib import admin
# from rango.about import views
from rango import views
from rango.about import views as views2

urlpatterns = patterns('',
		url(r'^$', views.index, name='rango'),
        url(r'^about/', views2.index, name='rango/about'),
        # url(r'^rango/', views.index, name='rango/'),
        # url(r'about/', include('about.urls')),
)