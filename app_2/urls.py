from django.conf.urls import url

from app_2 import views


urlpatterns = [
    url(r'^index/$', views.index, name='index-2'),
    url(r'^template_1/$', views.template_1, name='template_1-2'),
]
