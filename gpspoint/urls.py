"""gpspoint URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
url(r'^waypoint/', 'waypoint.views.index',name='index'),
url(r'^userdata/','userdata.views.Get_userdata',name='Get_userdata'),
url(r'^sensordata/','userdata.views.Get_sensordata',name='Get_sensordata'),
url(r'^emergency/','userdata.views.Get_emergencydata',name='Get_emergencydata'),
url(r'^hello/','waypoint.views.hello',name='hello'),
url(r'^test/','waypoint.views.test',name='test'),
url(r'^site_media/(?P<path>.*)','django.views.static.serve',{'document_root':'/home/zhao/www/gpspoint/waypoint/templates/pic'}),
]
