from django.conf.urls import url

from blog_app import views

app_name = 'blog_app'
urlpatterns = [
    url(r'^create/$', views.BlogCreateView, name='blog_create'),
    # url(r'^$', views.BlogListView.as_view(), name="login"),
    # url(r'^', views.BlogReadView.as_view(), name="login"),
    # url(r'^', views.BlogCreateView.as_view(), name="login"),
    # url(r'^', views.BlogDeleteView.as_view(), name="login"),

]
