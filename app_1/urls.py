from django.conf.urls import url

from app_1 import views


urlpatterns = [
    url(r'^index/$', views.index, name='index-1'),
    url(r'^template_1/$', views.template_1, name='template_1-1'),
    url(r'^template_2/$', views.template_2, name='template_2-1'),
]
